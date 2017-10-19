# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0009_auto_20171019_0211'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderserver',
            name='layer0',
            field=models.IntegerField(default=6),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='architectconfigpattern',
            name='filename',
            field=models.CharField(default=b'configpattern.tgz', max_length=32),
            preserve_default=True,
        ),
    ]
