# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0004_auto_20171014_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rack',
            name='expansion_racks',
            field=models.ForeignKey(blank=True, to='lxca.Rack', null=True),
            preserve_default=True,
        ),
    ]
