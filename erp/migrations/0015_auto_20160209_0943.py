# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0014_auto_20160208_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='myitem',
            name='SKU',
            field=models.CharField(max_length=32, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mycrm',
            name='crm_type',
            field=models.CharField(default=b'vendor', max_length=16, choices=[(b'B', b'Both'), (b'V', b'Vendor'), (b'C', b'Customer')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myitem',
            name='brand',
            field=models.ForeignKey(verbose_name='\u54c1\u724c', to='erp.MyCRM'),
            preserve_default=True,
        ),
    ]
