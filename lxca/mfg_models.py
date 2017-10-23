import uuid
import re
from ruamel import yaml
import simplejson as json
from django.db import models
from django_extensions.db.fields import UUIDField
from lxca.models import BaseModel


class BaremetalManager(models.Model):
    # BM manager, eg. LXCA
    user = models.CharField(max_length=64, default="")
    password = models.CharField(max_length=32, default="")
    url = models.URLField(default="")
    recovery_id = models.CharField(max_length=32, default="root")
    recovery_password = models.CharField(max_length=32, default="Passw0rd")

    def __unicode__(self):
        return "%s:%s@%s" % (self.user, self.password, self.url)


class MfgSolution(models.Model):
    order = models.ForeignKey("OrderSolution")
    bm_manager = models.ForeignKey("BaremetalManager",
                                   blank=True,
                                   null=True)

    def __unicode__(self):
        return self.order.__unicode__()

    def _racks(self):
        return MfgRack.objects.filter(mfg=self)
    racks = property(_racks)

    def _num_racks(self):
        return sum([s.order.qty for s in self.racks])
    num_racks = property(_num_racks)

    def _pdus(self):
        return MfgPdu.objects.filter(mfg=self)
    pdus = property(_pdus)

    def _num_pdus(self):
        return sum([s.order.qty for s in self.pdus])
    num_pdus = property(_num_pdus)

    def _switches(self):
        return MfgSwitch.objects.filter(mfg=self)
    switches = property(_switches)

    def _num_switches(self):
        return sum([s.order.qty for s in self.switches])
    num_switches = property(_num_switches)

    def _servers(self):
        return MfgServer.objects.filter(mfg=self)
    servers = property(_servers)

    def _num_servers(self):
        return sum([s.order.qty for s in self.servers])
    num_servers = property(_num_servers)

    def _manifest(self):
        solution = self.order.manifest["solution"]
        lxca = solution["lxca"].copy()
        lxca.update({
            "user": self.bm_manager.user,
            "password": self.bm_manager.password,
            "url": self.bm_manager.url,
            "recovery_id": self.bm_manager.recovery_id,
            "recovery_passwd": self.bm_manager.recovery_password
        })
        solution["lxca"] = lxca

        # pdus
        hosts = [{
            "Machine-Type-Model": pdu.order.template.catalog.name,
            "ip": pdu.ip4,
            "ip6": pdu.ip6,
            "name": pdu.username,
            "passwd": pdu.password,
            "imm": {
                "Machine-Type-Model": pdu.order.template.catalog.name,
                "Serial-Number": pdu.serial,
                "UUID": pdu.uuid,
                "ip": pdu.imm_ip,
                "user": pdu.imm_user,
                "passwd": pdu.imm_password
            }
        } for pdu in self.pdus]
        solution["hardware"]["pdus"] = hosts

        # switches
        hosts = [{
            "Machine-Type-Model": switch.order.template.catalog.name,
            "ip": switch.ip4,
            "ip6": switch.ip6,
            "name": switch.username,
            "passwd": switch.password,
            "imm": {
                "Machine-Type-Model": switch.order.template.catalog.name,
                "Serial-Number": switch.serial,
                "UUID": switch.uuid,
                "ip": switch.imm_ip,
                "user": switch.imm_user,
                "passwd": switch.imm_password
            }
        } for switch in self.switches]
        solution["hardware"]["switches"] = hosts

        # servers
        hosts = [{
            "Machine-Type-Model": server.order.template.catalog.name,
            "ip": server.ip4,
            "ip6": server.ip6,
            "name": server.username,
            "passwd": server.password,
            "imm": {
                "Machine-Type-Model": server.order.template.catalog.name,
                "Serial-Number": server.serial,
                "UUID": server.uuid,
                "ip": server.imm_ip,
                "user": server.imm_user,
                "passwd": server.imm_password
            }
        } for server in self.servers]
        solution["hardware"]["servers"] = hosts
        return {"solution": solution}
    manifest = property(_manifest)

    def _json_manifest(self):
        return json.dumps(self.manifest,
                          indent=4)
    json_manifest = property(_json_manifest)

    def _yaml_manifest(self):
        return yaml.dump(self.manifest,
                         Dumper=yaml.RoundTripDumper)
    yaml_manifest = property(_yaml_manifest)

    def _charm_bundle(self):
        pat = re.compile("[()\s]+")

        services = {}

        # dump lxca
        bm = self.bm_manager
        lxca = {
            "user": bm.user,
            "password": bm.password,
            "url": bm.url
        }

        # dump solution
        ref_solution = self.order.solution
        solution_charm_name = pat.sub("", ref_solution.name).lower()
        endpoints = []
        for aa in [self.racks, self.switches, self.servers]:
            for mfg in aa:
                my_catalog = mfg.order.template.catalog
                my_ref = mfg.order.template
                my_order = mfg.order
                endpoints.append({
                    "uuid": mfg.uuid,
                    "machine_type": "mtm",  # TODO: what is this!?
                    "endpoint_ip": mfg.ip4,
                    "manage_user": mfg.username,
                    "manage_password": mfg.password,
                    "recovery_password": self.bm_manager.recovery_password
                })
        uhm = {
            "lxca": lxca,
            "playbooks": ref_solution.playbook_bundle,
            "endpoints": endpoints
        }

        services[solution_charm_name] = {
            # https://github.com/juju/juju/pull/7537/files
            # all application name must be lower cased!
            "charm": str(ref_solution.charm),

            "num_units": 1,
            "options": {
                "name": ref_solution.name,
                "uuid": ref_solution.uuid,
                "mtm": "mtm",  # TODO: doesn't need this!
                "uhm": yaml.dump(uhm,
                                 Dumper=yaml.RoundTripDumper)
            },
            # TODO: hardcoded for now
            "to": ["1"]
        }

        # dump HW charms
        for aa in [self.racks, self.switches, self.servers]:
            for mfg in aa:
                my_catalog = mfg.order.template.catalog
                my_ref = mfg.order.template
                my_order = mfg.order

                uhm = {
                    "lxca": lxca,
                    "playbooks": my_ref.playbook_bundle,
                    "endpoints": {
                        "endpoint_ip": mfg.imm_ip,
                        "user": mfg.mfg.bm_manager.user,
                        "password": mfg.mfg.bm_manager.password,
                        "recovery_password": mfg.mfg.bm_manager.recovery_password
                    }
                }

                services[pat.sub("", my_catalog.name).lower()] = {
                    "charm": str(my_ref.charm),
                    "num_units": 1,
                    "options": {
                        "name": my_catalog.name,
                        "uuid": mfg.uuid,
                        "mtm": "mtm",
                        "uhm": uhm,
                        "uhm": yaml.dump(uhm,
                                         Dumper=yaml.RoundTripDumper),
                    },
                    # TODO: hardcoded for now
                    "to": ["1"]
                }

        # dump relations
        # TODO: the name of the `relation`, eg. `rack, `server`,
        # are what is defined in `metadata.yaml` in each charm.
        # I'm hardcoding them right now.
        # We need to build a model to map this info into this framework.
        relations = []

        # solution <-> rack
        for r in self.racks:
            provide = "%s:rack" % solution_charm_name
            require = "%s:solution" % pat.sub("", r.order.template.catalog.name)
            relations.append([provide.lower(), require.lower()])

        # rack <-> switch
        for r in self.racks:
            for s in self.switches:
                provide = "%s:switch" % pat.sub("", r.order.template.catalog.name)
                require = "%s:rack" % pat.sub("", s.order.template.catalog.name)
                relations.append([provide.lower(), require.lower()])

        # rack <-> sever
        for r in self.racks:
            for s in self.servers:
                provide = "%s:server" % pat.sub("", r.order.template.catalog.name)
                require = "%s:rack" % pat.sub("", s.order.template.catalog.name)
                relations.append([provide.lower(), require.lower()])

        # switch <-> sever
        for r in self.switches:
            for s in self.servers:
                provide = "%s:server" % pat.sub("", r.order.template.catalog.name)
                require = "%s:switch" % pat.sub("", s.order.template.catalog.name)
                relations.append([provide.lower(), require.lower()])

        # my bundle data
        return {
            # TODO: add a model for this info.
            # hardcoded for now.
            "machines": {
                "1": {
                    "series": "trusty"
                }
            },
            "series": "trusty",
            "services": services,
            "relations": relations
        }
    charm_bundle = property(_charm_bundle)

    def _json_bundle(self):
        return json.dumps(self.charm_bundle,
                          indent=4)
    json_bundle = property(_json_bundle)

    def _yaml_bundle(self):
        return yaml.dump(self.charm_bundle,
                         Dumper=yaml.RoundTripDumper,
                         indent=2)
    yaml_bundle = property(_yaml_bundle)


class MfgEndpoint(models.Model):
    mfg = models.ForeignKey("MfgSolution")

    # this is a traceable piece of HW
    # that is unique within the entire org!
    serial = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        verbose_name=u"Serial number"
    )
    uuid = UUIDField(default=uuid.uuid4)

    # imm
    imm_ip = models.GenericIPAddressField(
        blank=True, null=True,
        verbose_name=u"IMM IP4 address")
    imm_user = models.CharField(
        max_length=32,
        default="lenovo",
        blank=True, null=True,
        verbose_name=u"IMM user")
    imm_password = models.CharField(
        max_length=32, default="passw0rd",
        blank=True, null=True,
        verbose_name=u"IMM password")

    # regular access
    username = models.CharField(
        max_length=32, default="lxca",
        blank=True, null=True,
        verbose_name=u"Mgt user")
    password = models.CharField(
        max_length=32,
        default="Th1nkAg!le",
        blank=True, null=True,
        verbose_name=u"Mgt password")
    ip4 = models.GenericIPAddressField(
        blank=True,
        null=True,
        verbose_name=u"Mgt IP4 address")
    ip6 = models.GenericIPAddressField(
        blank=True,
        null=True,
        verbose_name=u"Mgt IP6 address")

    class Meta:
        abstract = True


class MfgRack(MfgEndpoint):
    order = models.ForeignKey("OrderRack")


class MfgPdu(MfgEndpoint):
    order = models.ForeignKey("OrderPdu")


class MfgSwitch(MfgEndpoint):
    order = models.ForeignKey("OrderSwitch")


class MfgServer(MfgEndpoint):
    order = models.ForeignKey("OrderServer")
