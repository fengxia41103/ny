# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0018_auto_20171017_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='architectapplication',
            name='description',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='architectapplication',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='architectapplication',
            name='name',
            field=models.CharField(default='default name', max_length=128),
            preserve_default=True,
        ),
    ]
