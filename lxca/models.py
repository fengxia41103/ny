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

OS_CHOICES = (
    ("win210svr", "Windows Server 2010"),
    ("esxi", "ESXI server"),
    ("Ubuntu xeniel", "Ubuntu 16.04 Xeniel"),
    ("Ubuntu trusty", "Ubuntu 14.04 Trusty")
)


class BaseModel (models.Model):
    # basic value fields
    name = models.CharField(
        default=u"default name",
        max_length=128,
    )
    description = models.TextField(default="")

    # help text
    help_text = models.CharField(
        null=True,
        blank=True,
        max_length=64,
        verbose_name=u"Help"
    )
    # is object active
    is_active = models.BooleanField(default=True)

    serial = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        verbose_name=u"Serial number"
    )
    # is debug active
    is_debug = models.BooleanField(default=False)

    uuid = models.CharField(max_length=32, default="uuid")
    mtm = models.CharField(max_length=64, default="mtm")

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
#	Hardware BOM models
#
#####################################################
class Rack(BaseModel):
    SIZE_CHOICES = (
        (u"16U", u"16U"),
        (u"32U", u"32U"),
        (u"48U", u"48U")
    )

    is_primary = models.BooleanField(
        default=True,
        verbose_name=u"Is primary rack"
    )
    size = models.CharField(
        max_length=8,
        default=u"16U",
        choices=SIZE_CHOICES
    )
    width = models.FloatField(
        default=19,
        verbose_name="Rack width (inch)"
    )


class EndpointModel(BaseModel):
    SIZE_CHOICES = (
        (u"1U", u"1U"),
        (u"2U", u"2U"),
    )
    size = models.CharField(
        max_length=8,
        default=u"1U",
        choices=SIZE_CHOICES
    )

    class Meta:
        abstract = True


class PDU(EndpointModel):
    VOLTAGE_CHOICES = (
        (u"120-1", u"120V single phase"),
        (u"208-1", u"208V single phase"),
        (u"120-3", u"208V three phase"),
        (u"400-3", u"400V three phase")
    )

    ORIENTATION_CHOICES = (
        (u"h", u"Horizontal"),
        (u"v", u"Vertical")
    )
    voltage = models.CharField(
        max_length=16,
        default=u"120-1",
        choices=VOLTAGE_CHOICES
    )
    orientation = models.CharField(
        max_length=16,
        default=u"h",
        choices=ORIENTATION_CHOICES
    )
    form_factor = models.IntegerField(
        default=1,
        verbose_name=u"Form factor",
        help_text=u"0=vertical mount, 1=1U, 2=2U, and so on"
    )


class Switch(EndpointModel):
    SPEED_CHOICES = (
        (u"1G", u"1G"),
        (u"10G", u"10G"),
    )
    COOLING_ORIENTATIONS = (
        (u"h", u"Horizontal"),
        (u"v", u"Vertical")
    )
    speed = models.CharField(
        max_length=8,
        default=u"1G",
        choices=SPEED_CHOICES
    )
    cooling_orientation = models.CharField(
        max_length=8,
        default=u"h",
        choices=COOLING_ORIENTATIONS,
        verbose_name=u"Cooling orientation"
    )
    rear_to_front = models.BooleanField(default=True)


class Server(EndpointModel):
    cpu_sockets = models.IntegerField(default=2)
    max_25_disk = models.IntegerField(default=12)
    max_35_disk = models.IntegerField(default=10)


class StorageDisk(models.Model):
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
    capacity_in_gb = models.IntegerField(
        default=100,
        help_text=u"Storage capacity in GB."
    )


class RaidAdapter(EndpointModel):
    SPEED_CHOICES = (
        ("PCIx1", "PCIx1"),
        ("PCIx4", "PCIx4"),
        ("PCIx6", "PCIx6"),

    )
    speed = models.CharField(
        max_length=32,
        choices=SPEED_CHOICES,
        default=u"PCIx1",
        verbose_name=u"PCI speed"
    )


######################################################
#
#	Solution architect  models
#
#####################################################


class Solution(BaseModel):
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        default=None,
        verbose_name=u"Solution"
    )
    manifestversion_major = models.CharField(max_length=8, default="0")
    manifestversion_minor = models.CharField(max_length=8, default="1")

    def _manifestversion(self):
        return ".".join([self.manifestversion_major, self.manifestversion_minor])
    manifestversion = property(_manifestversion)


class Application(models.Model):
    name = models.CharField(max_length=32)
    host = models.CharField(
        max_length=32,
        choices=OS_CHOICES
    )
    compatible_servers = models.ManyToManyField("Server")


class FirmwareRepo(models.Model):
    UPDATE_ACCESS_METHOD_CHOICES = (
        ("m", "manual"),
    )
    update_access_method = models.CharField(
        choices=UPDATE_ACCESS_METHOD_CHOICES,
        max_length=8,
        default="m"
    )
    update_access_location = models.FilePathField(
        path="/home/lenovo",
        match="foo.*",
        recursive=True
    )
    pack = models.FilePathField(
        path="/home/lenovo",
        match="pack[.]zip",
        recursive=True
    )
    fix = models.CharField(
        max_length=8,
        default="fixid"
    )


class FirmwareRepoPolicy(models.Model):
    name = models.CharField(max_length=32, default="repo policy")
    device = models.CharField(max_length=32, default="policity device")


######################################################
#
#    Order config  models
#
#####################################################
class OrderServerModel(models.Model):
    firmware = models.CharField(max_length=32, default="firmware version")
    cores = models.IntegerField(default=2)
    mem = models.IntegerField(
        default=16,
        help_text=u"Memory size in GB")

######################################################
#
#    UHM config  models
#
#####################################################


class ConfigBaseModel(models.Model):
    bm_user = models.CharField(max_length=64, default="")
    bm_password = models.CharField(max_length=32, default="")
    bm_manager_url = models.URLField(default="")
    playbooks = models.ManyToManyField("Playbook")

    imm_ip = models.GenericIPAddressField(blank=True, null=True)
    imm_user = models.CharField(max_length=64, default="")
    imm_password = models.CharField(max_length=32, default="")

    firmware_update = models.CharField(max_length=32, default="")
    config_pattern = models.CharField(max_length=32, default="")

    class Meta:
        abstract = True


class Playbook(models.Model):
    name = models.CharField(max_length=32)
    path = models.FilePathField()
    tags = models.CharField(max_length=32, default="")
    extra_vars = JSONField(default="")


class SolutionConfig(ConfigBaseModel):
    solution = models.ForeignKey("Solution")

    # solution is really an abstract concept
    # that groups racks
    racks = models.ManyToManyField("RackConfig")


class RackConfig(ConfigBaseModel):
    rack = models.ForeignKey("Rack")
    pdu_configs = models.ManyToManyField("PduConfig")
    switch_configs = models.ManyToManyField("SwitchConfig")
    server_configs = models.ManyToManyField("ServerConfig")
    storage_configs = models.ManyToManyField("StorageConfig")

    def _pdus(self):
        return [a.pdu for a in self.pdu_configs.all()]
    pdus = property(_pdus)

    def _switches(self):
        return [a.switch for a in self.switch_configs.all()]
    switches = property(_switches)

    def _servers(self):
        return [a.server for a in self.server_configs.all()]
    servers = property(_servers)

    def _storages(self):
        return [a.storage for a in self.storage_configs.all()]
    storages = property(_storages)


class PduConfig(ConfigBaseModel):
    pdu = models.ForeignKey("PDU")


class ServerConfig(ConfigBaseModel):
    server = models.ForeignKey("Server")
    operating_system = models.CharField(
        max_length=256,
        default="Ubuntu xeniel",
        choices=OS_CHOICES
    )


class SwitchConfig(ConfigBaseModel):
    switch = models.ForeignKey("Switch")


class RaidAdapterConfig(ConfigBaseModel):
    raid = models.ForeignKey("RaidAdapter")


class StorageConfig(ConfigBaseModel):
    storage = models.ForeignKey("StorageDisk")
