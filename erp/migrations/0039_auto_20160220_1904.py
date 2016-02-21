# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0038_auto_20160220_1718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mysalesorderfullfillment',
            name='abbrev',
        ),
        migrations.RemoveField(
            model_name='mysalesorderfullfillment',
            name='description',
        ),
        migrations.RemoveField(
            model_name='mysalesorderfullfillment',
            name='hash',
        ),
        migrations.RemoveField(
            model_name='mysalesorderfullfillment',
            name='help_text',
        ),
        migrations.RemoveField(
            model_name='mysalesorderfullfillment',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='mysalesorderfullfillment',
            name='name',
        ),
        migrations.AlterField(
            model_name='mybusinessmodel',
            name='sales_model',
            field=models.CharField(default=b'Retail', max_length=64, choices=[(b'Retail', b'Retail'), (b'Wholesale', b'Wholesale'), (b'Consignment', b'Consignment'), (b'Leasing', b'Leasing'), (b'Proxy', b'Proxy')]),
            preserve_default=True,
        ),
    ]
