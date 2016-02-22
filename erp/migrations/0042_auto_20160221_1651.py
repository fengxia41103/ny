# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0041_auto_20160221_1638'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mysalesorderpayment',
            old_name='useage',
            new_name='usage',
        ),
    ]
