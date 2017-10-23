from django.db import models
from annoying.fields import JSONField  # django-annoying
from django_extensions.db.fields import UUIDField
from ruamel import yaml
import uuid
import simplejson as json

from lxca.models import BaseModel
from lxca.orchestrator_models import *

######################################################
#
#	Solution architect  models
#
#####################################################


class Playbook(models.Model):
    FOR_TYPE_CHOICES = (
        (1, u"Solution"),
        (2, u"Rack"),
        (3, u"PDU"),
        (4, u"Switch"),
        (5, u"Server"),
        (6, u"Endpoint")
    )
    for_type = models.IntegerField(
        blank=True, null=True,
        choices=FOR_TYPE_CHOICES,
        default=5
    )
    name = models.CharField(max_length=32)
    comment = models.CharField(
        max_length=128, blank=True, default="")
    path = models.CharField(
        max_length=128,
        blank=True, null=True,
        default="")
    tags = models.CharField(max_length=32,
                            blank=True, null=True,
                            default="")
    extra_vars = JSONField(blank=True, null=True, default="")

    def __unicode__(self):
        return "/".join([
            self.get_for_type_display(),
            "_".join(self.name.split(" "))
        ])


class ArchitectSolution(BaseModel):
    uuid = UUIDField(default=uuid.uuid4)

    # allow solution chain
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        default=None,
    )

    # orchestrator
    charm = models.ForeignKey("MyCharm",
                              null=True, blank=True)
    playbooks = models.ManyToManyField("Playbook",
                                       null=True, blank=True)

    # everything else
    version = models.CharField(max_length=8, default="Alpha")
    lxca = models.ForeignKey("ArchitectLxca",
                             default=1)
    compliance = models.ForeignKey("ArchitectCompliance",
                                   default=1)
    firmware_repo = models.ForeignKey("ArchitectFirmwareRepo",
                                      default=1)

    # hardware
    powers = models.ManyToManyField("ArchitectPdu",
                                    null=True, blank=True)
    racks = models.ManyToManyField("ArchitectRack",
                                   null=True, blank=True)
    switches = models.ManyToManyField("ArchitectSwitch",
                                      null=True, blank=True)
    servers = models.ManyToManyField("ArchitectServer",
                                     null=True, blank=True)

    # software meets hardware! Picking application will determine
    # which servers are available to pick.
    applications = models.ManyToManyField("ArchitectApplication",
                                          blank=True, null=True)

    def _hosts(self):
        return [s.host for s in self.applications.all()]
    hosts = property(_hosts)

    def _compatible_servers(self):
        tmp = [s.compatible_servers.all() for s in self.applications.all()]
        return set(itertools.chain.from_iterable(tmp))
    compatible_servers = property(_compatible_servers)

    def _manifest(self):
        # solution template YAML
        return {"solution": {
            "name": self.name,
            "manifestversion": self.version,
            "hosts": self.hosts,
            "workloads": [a.name for a in self.applications.all()],
            "compliancepolicies": {
                "name": self.compliance.name,
                "rule": []
            },
            "firmwareRepository": {
                "updateAccess": self.firmware_repo.update_access_method,
                "packFileName": self.firmware_repo.pack_filename,
                "fixId": self.firmware_repo.fix_id
            },
            "lxca": {
                "version": self.lxca.version,
                "lxcaPatchUpdateFieldName": self.lxca.patch_update_filename
            },
            "hardware": {
                "servers": {
                    "machine_type": [
                        s.catalog.name for s in self.servers.all()],
                },
                "switches": {
                    "machine_type": [
                        s.catalog.name for s in self.switches.all()],
                },
                "racks": {
                    "machine_type": [
                        s.catalog.name for s in self.racks.all()],
                },
                "pdus": {
                    "machine_type": [s.catalog.name for s in self.powers.all()],
                }
            }
        }}
    manifest = property(_manifest)

    def _json_manifest(self):
        return json.dumps(self.manifest,
                          indent=4)
    json_manifest = property(_json_manifest)

    def _yaml_manifest(self):
        return yaml.dump(self.manifest,
                         Dumper=yaml.RoundTripDumper)
    yaml_manifest = property(_yaml_manifest)

    def _playbook_bundle(self):
        return {
            pb.name.replace(" ", "_"): {
                "path": pb.path,
                "vars": pb.extra_vars,
                "tags": pb.tags
            } for pb in self.playbooks.all()}
    playbook_bundle = property(_playbook_bundle)


class ArchitectCompliance(models.Model):
    name = models.CharField(
        max_length=32,
        default="compliance")

    def __unicode__(self):
        return self.name


class ArchitectLxca(models.Model):
    version = models.CharField(max_length=8)
    patch_update_filename = models.CharField(
        max_length=32,
        default="update.tgz")

    def __unicode__(self):
        return self.patch_update_filename


class ArchitectApplication(BaseModel):
    """Applications certified by SA

    These applications are somehow stamped by SA that can run on this
    architecture. Therefore, we can take an assumption that there are
    orchestration means to facilitate its installation and even
    life-cycle management.
    """
    PLATFORM_CHOICES = (
        ("bm", "BareMetal"),
        ("win210svr", "Windows Server 2010"),
        ("esxi", "ESXI server"),
        ("Ubuntu xeniel", "Ubuntu 16.04 Xeniel"),
        ("Ubuntu trusty", "Ubuntu 14.04 Trusty")
    )

    host = models.CharField(
        max_length=32,
        choices=PLATFORM_CHOICES
    )
    compatible_servers = models.ManyToManyField("CatalogServer")

    def __unicode__(self):
        return "%s on %s" % (self.name,
                             self.host)


class ArchitectFirmwareRepo(models.Model):
    UPDATE_ACCESS_METHOD_CHOICES = (
        ("m", "manual"),
    )
    update_access_method = models.CharField(
        choices=UPDATE_ACCESS_METHOD_CHOICES,
        max_length=1,
        default="m"
    )

    fix_id = models.CharField(
        max_length=8,
        default="fixpack"
    )
    pack_filename = models.CharField(
        max_length=32,
        default="fixpack.tgz")

    def __unicode__(self):
        return self.fix_id


class ArchitectRuleForCount(models.Model):
    max_count = models.IntegerField(default=0)
    min_count = models.IntegerField(default=0)

    def __unicode__(self):
        return "%d-%d" % (self.min_count, self.max_count)


class ArchitectConfigPattern(models.Model):
    filename = models.CharField(
        max_length=32,
        default="configpattern.tgz"
    )

    def __unicode__(self):
        return self.filename


class ArchitectEndpoint(models.Model):
    rule_for_count = models.ForeignKey("ArchitectRuleForCount")
    firmware_policy = models.CharField(max_length=32, default="")
    config_pattern = models.ForeignKey("ArchitectConfigPattern")

    # orchestrator
    charm = models.ForeignKey("MyCharm",
                              null=True, blank=True)
    playbooks = models.ManyToManyField("Playbook",
                                       null=True, blank=True)

    def _playbook_bundle(self):
        return {
            pb.name.replace(" ", "_"): {
                "path": pb.path,
                "vars": pb.extra_vars,
                "tags": pb.tags
            } for pb in self.playbooks.all()}
    playbook_bundle = property(_playbook_bundle)


class ArchitectRack(ArchitectEndpoint):
    catalog = models.ForeignKey("CatalogRack")

    def __unicode__(self):
        return "%s (%s)" % (self.catalog,
                            self.rule_for_count)


class ArchitectPdu(ArchitectEndpoint):
    catalog = models.ForeignKey("CatalogPdu")

    def __unicode__(self):
        return "%s (%s)" % (self.catalog,
                            self.rule_for_count)


class ArchitectSwitch(ArchitectEndpoint):
    catalog = models.ForeignKey("CatalogSwitch")

    def __unicode__(self):
        return "%s (%s)" % (self.catalog,
                            self.rule_for_count)


class ArchitectServer(ArchitectEndpoint):
    catalog = models.ForeignKey("CatalogServer")

    def _hosts(self):
        return [a.host for a in self.applications.all()]
    hosts = property(_hosts)

    def __unicode__(self):
        return "%s (%s)" % (self.catalog,
                            self.rule_for_count)
