# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0007_auto_20160208_1859'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyItemInventory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qty', models.IntegerField(default=0)),
                ('item', models.ForeignKey(to='erp.MyItem')),
                ('locations', models.ForeignKey(to='erp.MyLocation')),
                ('warehouses', models.ForeignKey(to='erp.MyWarehouse')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='myitem',
            name='locations',
        ),
        migrations.RemoveField(
            model_name='myitem',
            name='warehouses',
        ),
        migrations.AlterField(
            model_name='mywarehouse',
            name='company',
            field=models.ForeignKey(to='erp.MyLocation'),
            preserve_default=True,
        ),
    ]
