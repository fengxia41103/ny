# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0005_auto_20171014_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rack',
            name='expansion_racks',
            field=models.ForeignKey(default=None, blank=True, to='lxca.Rack', help_text=b'Expansion rack for the primary', null=True),
            preserve_default=True,
        ),
    ]
