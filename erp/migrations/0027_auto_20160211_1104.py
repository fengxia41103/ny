# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0026_mysalesorder_is_sell_at_cost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mysalesorder',
            old_name='is_sell_at_cost',
            new_name='is_sold_at_cost',
        ),
    ]
