import uuid
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
