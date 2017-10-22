from django.db import models
from annoying.fields import JSONField  # django-annoying
from ruamel import yaml
import uuid
import simplejson as json

from lxca.models import BaseModel


class MyCharm(models.Model):
    HOST_CHOICES = (
        (1, u"Ubuntu 16.04 Xeniel"),
        (2, u"Ubuntu 14.04 Trusty"),
        (3, u"Cent 7.0"),
        (4, u"RHEL 7.4")
    )
    host = models.IntegerField(default=2,
                               choices=HOST_CHOICES)
    name = models.CharField(max_length=32)
    relations = models.ManyToManyField("self", blank=True)

    def __unicode__(self):
        # if not implemented, leave it as None.
        host_mappings = {
            1: "xenial",
            2: "trusty",
            3: "centos7",
            4: "rhel74"
        }
        if self.host and host_mappings[self.host]:
            return "/".join([
                host_mappings[self.host],
                self.name
            ])
        else:
            return "[??]/" + self.name
