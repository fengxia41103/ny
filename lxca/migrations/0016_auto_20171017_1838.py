# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0015_auto_20171017_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pduoutput',
            name='power_limit_per_group',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
