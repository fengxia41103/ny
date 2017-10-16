# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0010_auto_20171014_2353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catalograck',
            old_name='sizewall_compartment',
            new_name='sidewall_compartment',
        ),
    ]
