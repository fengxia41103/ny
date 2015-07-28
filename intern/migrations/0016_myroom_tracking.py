# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0015_auto_20150727_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='myroom',
            name='tracking',
            field=models.CharField(default='', max_length=32, verbose_name='Custom tracking ID'),
            preserve_default=False,
        ),
    ]
