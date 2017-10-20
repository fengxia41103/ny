from django.db import models
from lxca.models import BaseModel

######################################################
#
#	Hardware catalog models
#
#####################################################


class CatalogRack(BaseModel):
    EIA_CAPACITY_CHOICES = (
        (25, u"25U"),
        (42, u"42U"),
    )

    is_primary = models.BooleanField(
        default=True,
        verbose_name=u"Is primary rack"
    )
    eia_capacity = models.IntegerField(
        default=25,
        choices=EIA_CAPACITY_CHOICES
    )
    sidewall_compartment = models.IntegerField(default=0)
    expansion_rack = models.ForeignKey("self",
                                       blank=True,
                                       null=True,
                                       default=None,
                                       help_text="Expansion rack for the primary")


class CatalogEndpoint(BaseModel):
    SIZE_CHOICES = (
        (0, u"0U"),
        (1, u"1U"),
        (2, u"2U"),
    )
    size = models.IntegerField(
        default=1,
        choices=SIZE_CHOICES
    )
    ORIENTATION_CHOICES = (
        (u"h", u"Horizontal"),
        (u"v", u"Vertical")
    )
    orientation = models.CharField(
        max_length=16,
        default=u"h",
        choices=ORIENTATION_CHOICES
    )

    class Meta:
        abstract = True


class PduInput(models.Model):
    """PDU input voltage, phase, current.
    https://lenovopress.com/redp5267.pdf
    """
    PHASE_CHOICES = (
        (1, u"1 Phase"),
        (3, u"3 Phase")
    )
    phase = models.IntegerField(
        default=1,
        choices=PHASE_CHOICES
    )

    FREQUENCY_CHOICES = (
        (1, u"50-60Hz"),
    )
    frequency = models.IntegerField(
        default=1,
        choices=FREQUENCY_CHOICES
    )

    class Meta:
        unique_together = ("phase", "frequency")

    def __unicode__(self):
        return " ".join([
            "%s" % self.get_phase_display(),
            "%s" % self.get_frequency_display()
        ])


class PduOutput(models.Model):
    """PDU out voltage, phase, current.
    https://lenovopress.com/redp5267.pdf
    """
    voltage = models.IntegerField(default=120)
    power_limit_per_pdu = models.IntegerField()
    power_limit_per_outlet = models.IntegerField()
    power_limit_per_group = models.IntegerField(
        null=True,
        blank=True
    )

    def _capacity(self):
        return self.voltage * self.power_limit_per_pdu
    capacity = property(_capacity)

    class Meta:
        unique_together = ("voltage",
                           "power_limit_per_pdu",
                           "power_limit_per_outlet",
                           "power_limit_per_group")

    def __unicode__(self):
        if self.power_limit_per_group:
            tmp = "%dA" % self.power_limit_per_group
        else:
            tmp = "-"
        return "/".join([
            "%dVAC" % self.voltage,
            "%dW" % self.capacity,
            "%dA" % self.power_limit_per_pdu,
            "%dA" % self.power_limit_per_outlet,
            "%s" % tmp
        ])


class CatalogPdu(CatalogEndpoint):
    c13 = models.IntegerField(default=0)
    c19 = models.IntegerField(default=0)

    # input only specify phase and frequency,
    # so it is 1-N relation.
    # The range of voltages and currents are
    # derived from selected outputs.
    input = models.ForeignKey(PduInput)
    outputs = models.ManyToManyField(PduOutput)
    is_monitored = models.BooleanField(default=False)

    def _input_voltages(self):
        voltages = [i.voltage for i in self.outputs.all()]
        min_vol = min(voltages)
        max_vol = max(voltages)
        return "%d-%dVAC" % (min_val, max_val)
    input_voltages = property(_input_voltages)

    def _input_currents(self):
        currents = [i.current for i in self.outputs.all()]
        min_vol = min(currents)
        max_vol = max(currents)
        return "%d-%dVAC" % (min_val, max_val)
    input_currents = property(_input_currents)


class CatalogSwitch(CatalogEndpoint):
    SPEED_CHOICES = (
        (1, u"1G"),
        (10, u"10G"),
    )
    speed = models.IntegerField(
        default=10,
        choices=SPEED_CHOICES
    )
    rear_to_front = models.BooleanField(default=True)


class CatalogServer(CatalogEndpoint):
    cpu_sockets = models.IntegerField(default=2)
    max_25_disk = models.IntegerField(
        default=12,
        help_text=u"Maximum number of 2.5inch disks")
    max_35_disk = models.IntegerField(default=10)


class CatalogStorageDisk(models.Model):
    CAPACITY_UNIT_CHOICES = (
        (u"GB", u"GB"),
        (u"TB", u"TB")
    )
    FORMAT_CHOICES = (
        ("2.5", "2.5 inch"),
        ("3.5", "3.5 inch"),
        ("ssd", "ssd")
    )
    physical_format = models.CharField(
        choices=FORMAT_CHOICES,
        max_length=8,
        default="2.5"
    )
    capacity = models.IntegerField(
        default=100,
        help_text=u"Storage capacity in GB."
    )

    def __unicode__(self):
        return "%s, %dGB" % (self.physical_format, self.capacity)


class CatalogRaidAdapter(CatalogEndpoint):
    SPEED_CHOICES = (
        (1, "PCIx1"),
        (4, "PCIx4"),
        (6, "PCIx6"),

    )
    speed = models.IntegerField(
        choices=SPEED_CHOICES,
        default=1,
        verbose_name=u"PCI speed"
    )
