# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0004_auto_20151209_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycurrency',
            name='name',
            field=models.CharField(max_length=16, verbose_name='Currency name'),
            preserve_default=True,
        ),
    ]
