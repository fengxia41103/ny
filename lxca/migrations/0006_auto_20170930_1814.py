# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0005_auto_20170930_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playbook',
            name='path',
            field=models.FilePathField(),
            preserve_default=True,
        ),
    ]
