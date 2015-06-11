# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0010_auto_20150611_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='myapplication',
            name='additional',
            field=models.TextField(default=b'', verbose_name='Additional info'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myapplication',
            name='budget',
            field=models.IntegerField(default=0, verbose_name='Allocated budget'),
            preserve_default=True,
        ),
    ]
