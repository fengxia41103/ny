# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0037_auto_20160218_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myitem',
            name='order_deadline',
        ),
        migrations.AddField(
            model_name='myvendoritem',
            name='delivery_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myvendoritem',
            name='minimal_qty',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myvendoritem',
            name='order_deadline',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
