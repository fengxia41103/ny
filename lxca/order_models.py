from django.db import models
from django_extensions.db.fields import UUIDField
from lxca.models import BaseModel
from ruamel import yaml
import uuid
import simplejson as json

######################################################
#
#    Order & BOM models
#
#####################################################


class OrderSolution(models.Model):
    order = models.CharField(max_length=32,
                             default="21873",
                             unique=True,
                             help_text=u"Order number")
    solution = models.ForeignKey("ArchitectSolution")

    ORDER_STATUS_CHOICES = (
        (1, u"draft"),  # in shopping cart
        (2, u"in MFG"),
        (3, u"in provisioning"),
        (4, u"in deployment"),
        (5, u"obsolete")
    )
    status = models.IntegerField(
        default=1,
        choices=ORDER_STATUS_CHOICES
    )

    def __unicode__(self):
        return "%s [#%s]" % (self.solution, self.order)

    def _applications(self):
        return OrderApplication.objects.filter(order=self)
    applications = property(_applications)

    def _racks(self):
        return OrderRack.objects.filter(order=self)
    racks = property(_racks)

    def _num_racks(self):
        return sum([s.qty for s in self.racks])
    num_racks = property(_num_racks)

    def _pdus(self):
        return OrderPdu.objects.filter(order=self)
    pdus = property(_pdus)

    def _num_pdus(self):
        return sum([s.qty for s in self.pdus])
    num_pdus = property(_num_pdus)

    def _switches(self):
        return OrderSwitch.objects.filter(order=self)
    switches = property(_switches)

    def _num_switches(self):
        return sum([s.qty for s in self.switches])
    num_switches = property(_num_switches)

    def _servers(self):
        return OrderServer.objects.filter(order=self)
    servers = property(_servers)

    def _num_servers(self):
        return sum([s.qty for s in self.servers])
    num_servers = property(_num_servers)

    def _manifest(self):
        solution = self.solution.manifest["solution"]
        solution["productdata"] = {
            "order": self.order,
            "uuid": str(uuid.uuid4()),
        }
        solution["hardware"]["pdus"] = [{
            "machine_type": [pdu.template.catalog.name],
            "qty": pdu.qty,
            "rules":{
                "max": pdu.template.rule_for_count.max_count,
                "min": pdu.template.rule_for_count.min_count,
            }
        } for pdu in self.pdus.all()]
        solution["hardware"]["switches"] = [{
            "machine_type": [switch.template.catalog.name],
            "qty": switch.qty,
            "rules":{
                "max": pdu.template.rule_for_count.max_count,
                "min": pdu.template.rule_for_count.min_count,
            }
        } for switch in self.switches.all()]
        solution["hardware"]["servers"] = [{
            "machine_type": [server.template.catalog.name],
            "qty": server.qty,
            "layer0": server.layer0,
            "rules":{
                "max": pdu.template.rule_for_count.max_count,
                "min": pdu.template.rule_for_count.min_count,
            }
        } for server in self.servers.all()]
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


class OrderEndpointModel(models.Model):
    """Common configurations that will be determined at ordering.
    """
    order = models.ForeignKey("OrderSolution")
    qty = models.IntegerField(default=1)


class OrderApplication(OrderEndpointModel):
    template = models.ForeignKey("ArchitectApplication",
                                 on_delete=models.CASCADE)

    def __unicode__(self):
        return "%s/%s" % (self.order, self.template.catalog)


class OrderRack(OrderEndpointModel):
    template = models.ForeignKey("ArchitectRack",
                                 on_delete=models.CASCADE)

    def __unicode__(self):
        return "%s/%s" % (self.order, self.template.catalog)


class OrderPdu(OrderEndpointModel):
    template = models.ForeignKey("ArchitectPdu",
                                 on_delete=models.CASCADE)

    def __unicode__(self):
        return "%s/%s" % (self.order, self.template.catalog)


class OrderSwitch(OrderEndpointModel):
    template = models.ForeignKey("ArchitectSwitch",
                                 on_delete=models.CASCADE)

    def __unicode__(self):
        return "%s/%s" % (self.order, self.template.catalog)


class OrderServer(OrderEndpointModel):
    """Server model in Ordering phase.

    Based on SA specifics, client can configure his server with
    more specifics such as the num of cores, memory size, disk size and so on.
    """
    template = models.ForeignKey("ArchitectServer")

    firmware = models.CharField(max_length=32, default="firmware version")
    cores = models.IntegerField(default=2)
    mem = models.IntegerField(
        default=16,
        help_text=u"Memory size in GB")
    storages = models.ManyToManyField("CatalogStorageDisk", blank=True)

    LAYER0_CHOICES = (
        (1, u"Windows Server 2010"),
        (2, u"ESXI server"),
        (3, u"Ubuntu 16.04 Xeniel"),
        (4, u"Ubuntu 14.04 Trusty"),
        (5, u"Cent 7.0"),
        (6, u"RHEL 7.4")
    )
    layer0 = models.IntegerField(default=6)
