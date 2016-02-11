# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0024_auto_20160211_0949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mysalesorderlineitem',
            name='fullfill_rate',
        ),
        migrations.RemoveField(
            model_name='mysalesorderlineitem',
            name='fullfilled',
        ),
        migrations.RemoveField(
            model_name='mysalesorderlineitem',
            name='size',
        ),
        migrations.RemoveField(
            model_name='mysalesorderlineitem',
            name='value',
        ),
        migrations.AlterField(
            model_name='mysalesorderfullfillment',
            name='po',
            field=models.ForeignKey(blank=True, to='erp.MyPurchaseOrder', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mysalesorderfullfillmentlineitem',
            name='po_line_item',
            field=models.ForeignKey(blank=True, to='erp.MyPurchaseOrderLineItem', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mysalesorderlineitem',
            name='item',
            field=models.ForeignKey(to='erp.MyItemInventory'),
            preserve_default=True,
        ),
    ]
