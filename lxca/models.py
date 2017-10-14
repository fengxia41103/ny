# -*- coding: utf-8 -*-

import logging
from datetime import datetime as dt

from annoying.fields import JSONField  # django-annoying
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.generic import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone

logger = logging.getLogger("lenovo-lxca")
logger.setLevel(logging.DEBUG)


class BaseModel (models.Model):
    # basic value fields
    name = models.CharField(
        default=u"default name",
        max_length=128,
    )
    description = models.TextField(default="")

    # is object active
    is_active = models.BooleanField(default=True)

    # attachments
    attachments = GenericRelation("Attachment")
    notes = GenericRelation("Note")

    # this is an Abstract model
    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name

######################################################
#
#	Tags
#
#####################################################


class TaggedItem (models.Model):
    # basic value fields
    tag = models.SlugField(
        default="",
        max_length=16,
        verbose_name=u"Tag"
    )

    def __unicode__(self):
        return self.tag

######################################################
#
#	Attachments
#
#####################################################


class Attachment (models.Model):
    # generic foreign key to base model
    # so we can link attachment to any model defined below
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    # instance fields
    created_by = models.ForeignKey(
        User,
        blank=True,
        null=True,
        default=None,
        verbose_name=u"Creator",
        help_text=""
    )

    # basic value fields
    name = models.CharField(
        default="default name",
        max_length=64,
    )
    description = models.CharField(
        max_length=64,
        default="default description",
    )
    file = models.FileField(
        upload_to="%Y/%m/%d",
        verbose_name=u"Attachment",
    )

    def __unicode__(self):
        return self.file.name

######################################################
#
#	Notes
#
#####################################################


class Note(models.Model):
    # generic foreign key to base model
    # so we can link attachment to any model defined below
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    content = models.TextField(
        verbose_name=u"Note"
    )


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
    sizewall_compartment = models.IntegerField(default=0)
    expansion_racks = models.ForeignKey("self",
                                        blank=True,
                                        null=True,
                                        default=None,
                                        help_text="Expansion rack for the primary")


class CatalogEndpoint(BaseModel):
    SIZE_CHOICES = (
        (u"1U", u"1U"),
        (u"2U", u"2U"),
    )
    size = models.CharField(
        max_length=8,
        default=u"1U",
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


class CatalogPdu(CatalogEndpoint):
    VOLTAGE_CHOICES = (
        (u"120-1", u"120V single phase"),
        (u"208-1", u"208V single phase"),
        (u"120-3", u"208V three phase"),
        (u"400-3", u"400V three phase")
    )
    voltage = models.CharField(
        max_length=16,
        default=u"120-1",
        choices=VOLTAGE_CHOICES
    )


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
    max_25_disk = models.IntegerField(default=12,
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


######################################################
#
#	Solution architect  models
#
#####################################################


class ArchitectSolution(BaseModel):
    # allow solution chain
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        default=None,
    )

    version = models.CharField(max_length=8)

    # firmware
    firmware_repo = models.ForeignKey("ArchitectFirmwareRepo")
    firmware_policy = models.ForeignKey("ArchitectFirmwareRepoPolicy")

    # software meets hardware! Picking application will determine
    # which servers are available to pick.
    applications = models.ManyToManyField("ArchitectApplication")

    def _hosts(self):
        return [s.host for s in self.applications.all()]
    hosts = property(_hosts)

    def _compatible_servers(self):
        tmp = [s.compatible_servers for s in self.workloads.all()]
        return set(reduce(lambda x, y: x + y, tmp))
    compatible_servers = property(_compatible_servers)

    # hardware
    racks = models.ManyToManyField("ArchitectRack")
    switches = models.ManyToManyField("ArchitectSwitch")
    servers = models.ManyToManyField("ArchitectServer")


class ArchitectApplication(models.Model):
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

    name = models.CharField(max_length=32)
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
    firmware_fix_id = models.CharField(
        max_length=8,
        default="fixid"
    )
    update_access_method = models.CharField(
        choices=UPDATE_ACCESS_METHOD_CHOICES,
        max_length=8,
        default="m"
    )
    update_access_location = models.FilePathField(
        path="/home/lenovo",
        match="foo.*",
        recursive=True,
        null=True,
        blank=True
    )
    firmware_pack = models.FilePathField(
        path="/home/lenovo",
        match="pack[.]zip",
        recursive=True,
        null=True,
        blank=True
    )

    def __unicode__(self):
        return self.firmware_fix_id


class ArchitectFirmwareRepoPolicy(models.Model):
    name = models.CharField(max_length=32, default="repo policy")
    device = models.CharField(max_length=32, default="policity device")

    def __unicode__(self):
        return self.name


class ArchitectRuleForCount(models.Model):
    max_count = models.IntegerField(default=0)
    min_count = models.IntegerField(default=0)

    def __unicode__(self):
        return "%d-%d" % (self.min_count, self.max_count)


class ArchitectRack(models.Model):
    catalog = models.ForeignKey("CatalogRack")
    rule_for_count = models.ForeignKey("ArchitectRuleForCount")

    def __unicode__(self):
        return "%s (%s)" % (self.catalog,
                            self.rule_for_count)


class ArchitectSwitch(models.Model):
    catalog = models.ForeignKey("CatalogSwitch")
    rule_for_count = models.ForeignKey("ArchitectRuleForCount")

    def __unicode__(self):
        return "%s (%s)" % (self.catalog,
                            self.rule_for_count)


class ArchitectServer(models.Model):
    catalog = models.ForeignKey("CatalogServer")
    rule_for_count = models.ForeignKey("ArchitectRuleForCount")

    def _hosts(self):
        return [a.host for a in self.applications.all()]
    hosts = property(_hosts)

    def __unicode__(self):
        return "%s (%s)" % (self.catalog,
                            self.rule_for_count)

######################################################
#
#    Order models
#
#####################################################


class MyOrder(models.Model):
    order = models.CharField(max_length=32,
                             default="21873",
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

    def _racks(self):
        return OrderRack.objects.filter(solution=self.solution)
    racks = property(_racks)

    def _switches(self):
        return OrderSwitch.objects.filter(solution=self.solution)
    switchs = property(_switches)

    def _servers(self):
        return OrderServer.objects.filter(solution=self.solution)
    servers = property(_servers)


class OrderBaseModel(models.Model):
    """Common configurations that will be determined at ordering.
    """
    order = models.ForeignKey("MyOrder")
    count = models.IntegerField(default=1)


class OrderRack(OrderBaseModel):
    template = models.ForeignKey("ArchitectRack")

    def __unicode__(self):
        return "%s/%s" % (self.order, self.template.catalog)


class OrderSwitch(OrderBaseModel):
    template = models.ForeignKey("ArchitectSwitch")

    def __unicode__(self):
        return "%s/%s" % (self.order, self.template.catalog)


class OrderServer(OrderBaseModel):
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
    ip = models.GenericIPAddressField(null=True, blank=True)
    storages = models.ManyToManyField("CatalogStorageDisk")

    def __unicode__(self):
        return "%s/%s" % (self.order, self.template.catalog)


######################################################
#
#    BOM models
#
#####################################################


class MfgSolution(models.Model):
    racks = models.ManyToManyField("MfgRack")
    switches = models.ManyToManyField("MfgSwitch")
    servers = models.ManyToManyField("MfgServer")


class MfgBaseModel(models.Model):
    # BM manager, eg. LXCA
    bm_user = models.CharField(max_length=64, default="")
    bm_password = models.CharField(max_length=32, default="")
    bm_manager_url = models.URLField(default="")

    # imm seetings
    imm_ip = models.GenericIPAddressField(blank=True, null=True)
    imm_user = models.CharField(max_length=64, default="")
    imm_password = models.CharField(max_length=32, default="")

    serial = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        verbose_name=u"Serial number"
    )
    uuid = models.CharField(max_length=32, default="uuid")
    mtm = models.CharField(max_length=64,
                           default="",
                           help_text="Machine type model")
    firmware_update = models.CharField(max_length=32, default="")
    config_pattern = models.CharField(max_length=32, default="")

    class Meta:
        abstract = True


class MfgRack(MfgBaseModel):
    on_order = models.ForeignKey("OrderRack")


class MfgSwitch(MfgBaseModel):
    on_order = models.ForeignKey("OrderSwitch")


class MfgServer(MfgBaseModel):
    on_order = models.ForeignKey("OrderServer")

######################################################
#
#    UHM config  models
#
#####################################################


class Playbook(models.Model):
    name = models.CharField(max_length=32)
    path = models.FilePathField()
    tags = models.CharField(max_length=32, default="")
    extra_vars = JSONField(default="")
