# -*- coding: utf-8 -*-
from __future__ import absolute_import

import codecs
import cPickle
import csv
import datetime as dt
import hashlib
import logging
import os
import re
import sys
import time
from datetime import timedelta
from decimal import Decimal
from itertools import izip_longest
from math import cos
from math import sin
from random import randint
from random import shuffle
from subprocess import check_output
from tempfile import NamedTemporaryFile

import lxml.html
import numpy as np
import pytz
import simplejson as json
from celery import shared_task
from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import User
from django.core.files import File
from lxml.html.clean import clean_html

from lxca.mfg_models import *
from ruamel import yaml

logger = logging.getLogger('lxca')


def grouper(iterable, n, padvalue=None):
    # grouper('abcdefg', 3, 'x') --> ('a','b','c'), ('d','e','f'),
    # ('g','x','x')
    return list(izip_longest(*[iter(iterable)] * n, fillvalue=padvalue))


@shared_task
def orchestrate_me(mfg_solution_id):
    mfg = MfgSolution.objects.get(pk=int(mfg_solution_id))
    bundle_yaml = NamedTemporaryFile(delete=False, mode="wt")
    bundle_yaml.write(mfg.yaml_bundle)
    bundle_yaml.close()
    check_output(["python", "deploy.py",
                  "--deployer", "bot", bundle_yaml.name])
