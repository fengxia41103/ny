# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0009_auto_20171014_1753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='architectsolution',
            name='help_text',
        ),
        migrations.RemoveField(
            model_name='catalogpdu',
            name='help_text',
        ),
        migrations.RemoveField(
            model_name='catalograck',
            name='help_text',
        ),
        migrations.RemoveField(
            model_name='catalograidadapter',
            name='help_text',
        ),
        migrations.RemoveField(
            model_name='catalogserver',
            name='help_text',
        ),
        migrations.RemoveField(
            model_name='catalogswitch',
            name='help_text',
        ),
        migrations.AlterField(
            model_name='catalogserver',
            name='max_25_disk',
            field=models.IntegerField(default=12, help_text='Maximum number of 2.5inch disks'),
            preserve_default=True,
        ),
    ]
