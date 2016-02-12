# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0028_mysalesorder_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mycrm',
            old_name='home_currency',
            new_name='currency',
        ),
    ]
