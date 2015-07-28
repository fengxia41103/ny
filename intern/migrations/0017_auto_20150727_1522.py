# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0016_myroom_tracking'),
    ]

    operations = [
        migrations.AddField(
            model_name='mybox',
            name='tracking',
            field=models.CharField(max_length=32, null=True, verbose_name='Custom tracking ID', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myroom',
            name='tracking',
            field=models.CharField(max_length=32, null=True, verbose_name='Custom tracking ID', blank=True),
            preserve_default=True,
        ),
    ]
