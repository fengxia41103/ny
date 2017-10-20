# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0009_auto_20171019_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playbook',
            name='path',
            field=models.CharField(default=b'', max_length=128, null=True, blank=True),
            preserve_default=True,
        ),
    ]
