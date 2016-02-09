# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_auto_20151209_0441'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyVendorItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sku', models.CharField(default=b'', max_length=32)),
                ('price', models.FloatField(default=0)),
                ('discount', models.FloatField(default=0.0)),
                ('vendor', models.ForeignKey(to='erp.MyVendor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='myitem',
            name='vendors',
        ),
        migrations.AddField(
            model_name='myitem',
            name='sources',
            field=models.ForeignKey(default='', to='erp.MyVendorItem'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myvendor',
            name='home_currency',
            field=models.ForeignKey(default='', to='erp.MyCurrency'),
            preserve_default=False,
        ),
    ]
