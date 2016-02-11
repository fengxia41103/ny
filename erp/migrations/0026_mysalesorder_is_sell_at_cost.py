# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0025_auto_20160211_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='mysalesorder',
            name='is_sell_at_cost',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
