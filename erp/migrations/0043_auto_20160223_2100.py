# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0042_auto_20160221_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mybusinessmodel',
            name='sales_model',
            field=models.CharField(default=b'Retail', max_length=64, choices=[(b'Retail', '\u96f6\u552e'), (b'Wholesale', '\u6279\u53d1'), (b'Consignment', '\u4ee3\u9500'), (b'Leasing', '\u79df\u8d41'), (b'Proxy', '\u8ba2\u8d27')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mycrm',
            name='std_discount',
            field=models.FloatField(default=0.25, validators=[django.core.validators.MaxValueValidator(1.0), django.core.validators.MinValueValidator(0.0)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myitem',
            name='price',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myiteminventory',
            name='physical',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mysalesorder',
            name='discount',
            field=models.FloatField(validators=[django.core.validators.MaxValueValidator(1.0), django.core.validators.MinValueValidator(0.0)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mysalesorderfullfillmentlineitem',
            name='fullfill_qty',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mysalesorderlineitem',
            name='qty',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=True,
        ),
    ]
