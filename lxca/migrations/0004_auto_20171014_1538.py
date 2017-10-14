# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0003_auto_20171014_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rack',
            name='eia_capacity',
            field=models.IntegerField(default=25, choices=[(25, '25U'), (42, '42U')]),
            preserve_default=True,
        ),
    ]
