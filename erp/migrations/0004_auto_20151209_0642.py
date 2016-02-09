# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0003_auto_20151209_0506'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mycurrency',
            old_name='abbreviation',
            new_name='abbrev',
        ),
    ]
