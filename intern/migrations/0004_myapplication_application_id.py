# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0003_auto_20150609_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='myapplication',
            name='application_id',
            field=models.CharField(max_length=64, null=True, verbose_name='Application ID', blank=True),
            preserve_default=True,
        ),
    ]
