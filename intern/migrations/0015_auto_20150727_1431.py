# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0014_auto_20150727_1427'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myitem',
            old_name='home_room',
            new_name='room',
        ),
        migrations.AddField(
            model_name='mybox',
            name='room',
            field=models.ForeignKey(verbose_name='Home room', blank=True, to='intern.MyRoom', null=True),
            preserve_default=True,
        ),
    ]
