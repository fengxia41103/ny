# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0011_auto_20171016_1744'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catalograck',
            old_name='expansion_racks',
            new_name='expansion_rack',
        ),
    ]
