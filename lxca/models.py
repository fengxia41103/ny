# -*- coding: utf-8 -*-

import logging
from datetime import datetime as dt
import itertools
from ruamel import yaml
import uuid

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
from django_extensions.db.fields import UUIDField

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
#    UHM config  models
#
#####################################################

class BaremetalManager(models.Model):
    # BM manager, eg. LXCA
    user = models.CharField(max_length=64, default="")
    password = models.CharField(max_length=32, default="")
    url = models.URLField(default="")

    def __unicode__(self):
        return self.url


class MfgSolution(models.Model):
    order = models.ForeignKey("OrderSolution")
    bm_manager = models.ForeignKey("BaremetalManager",
                                   blank=True,
                                   null=True)


class MfgEndpoint(models.Model):
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
    solution = models.ForeignKey("MfgSolution")
    order = models.ForeignKey("OrderRack")


class MfgPdu(MfgEndpoint):
    solution = models.ForeignKey("MfgSolution")
    order = models.ForeignKey("OrderPdu")


class MfgSwitch(MfgEndpoint):
    solution = models.ForeignKey("MfgSolution")
    order = models.ForeignKey("OrderSwitch")


class MfgServer(MfgEndpoint):
    solution = models.ForeignKey("MfgSolution")
    order = models.ForeignKey("OrderServer")
