# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0020_auto_20150727_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myitem',
            name='rooms',
        ),
        migrations.AddField(
            model_name='myitem',
            name='room',
            field=models.ForeignKey(verbose_name='Home room', blank=True, to='intern.MyRoom', null=True),
            preserve_default=True,
        ),
    ]
