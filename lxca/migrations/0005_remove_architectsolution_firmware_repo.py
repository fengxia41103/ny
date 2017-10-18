# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0004_auto_20171018_1919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='architectsolution',
            name='firmware_repo',
        ),
    ]
