# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('erp', '0010_auto_20160208_1935'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyCRM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hash', models.CharField(default=b'', max_length=256, null=True, verbose_name='MD5 hash', blank=True)),
                ('name', models.CharField(default=None, max_length=128, verbose_name='\u540d\u79f0')),
                ('description', models.TextField(null=True, verbose_name='\u63cf\u8ff0', blank=True)),
                ('abbrev', models.CharField(max_length=8, null=True, verbose_name='Abbreviation', blank=True)),
                ('help_text', models.CharField(max_length=64, null=True, verbose_name='\u5e2e\u52a9\u63d0\u793a', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('crm_type', models.CharField(default=b'vendor', max_length=16, choices=[(b'both', b'both'), (b'vendor', b'vendor'), (b'customer', b'customer')])),
                ('contact', models.CharField(max_length=32, null=True, verbose_name='CRM contact', blank=True)),
                ('phone', models.CharField(max_length=16, null=True, verbose_name='Vendor phone', blank=True)),
                ('balance', models.FloatField(default=0)),
                ('std_discount', models.FloatField(default=0.25)),
                ('home_currency', models.ForeignKey(to='erp.MyCurrency')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MyPurchaseOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hash', models.CharField(default=b'', max_length=256, null=True, verbose_name='MD5 hash', blank=True)),
                ('name', models.CharField(default=None, max_length=128, verbose_name='\u540d\u79f0')),
                ('description', models.TextField(null=True, verbose_name='\u63cf\u8ff0', blank=True)),
                ('abbrev', models.CharField(max_length=8, null=True, verbose_name='Abbreviation', blank=True)),
                ('help_text', models.CharField(max_length=64, null=True, verbose_name='\u5e2e\u52a9\u63d0\u793a', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('created_by', models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL, blank=True, help_text=b'', null=True, verbose_name='\u521b\u5efa\u7528\u6237')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MyPurchaseOrderLineItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('invoiced_qty', models.IntegerField(default=0)),
                ('packinglist_qty', models.IntegerField(default=0)),
                ('available_in', models.CharField(blank=True, max_length=8, null=True, choices=[('UNKNOWN', 'UNKNOWN'), ('LOCAL', 'LOCAL'), ('NEVER', 'NEVER'), ('JAN', 'JAN'), ('FEB', 'FEB'), ('MAR', 'MAR'), ('APR', 'APR'), ('MAY', 'MAY'), ('JUN', 'JUN'), ('JUL', 'JUL'), ('AUG', 'AUG'), ('SEP', 'SEP'), ('OCT', 'OCT'), ('NOV', 'NOV'), ('DEC', 'DEC')])),
                ('po', models.ForeignKey(to='erp.MyPurchaseOrder')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MySalesOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('discount', models.FloatField(default=0)),
                ('created_by', models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL, blank=True, help_text=b'', null=True, verbose_name='\u521b\u5efa\u7528\u6237')),
                ('customer', models.ForeignKey(to='erp.MyCRM')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MySalesOrderFullfillment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hash', models.CharField(default=b'', max_length=256, null=True, verbose_name='MD5 hash', blank=True)),
                ('name', models.CharField(default=None, max_length=128, verbose_name='\u540d\u79f0')),
                ('description', models.TextField(null=True, verbose_name='\u63cf\u8ff0', blank=True)),
                ('abbrev', models.CharField(max_length=8, null=True, verbose_name='Abbreviation', blank=True)),
                ('help_text', models.CharField(max_length=64, null=True, verbose_name='\u5e2e\u52a9\u63d0\u793a', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('created_by', models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL, blank=True, help_text=b'', null=True, verbose_name='\u521b\u5efa\u7528\u6237')),
                ('po', models.ForeignKey(to='erp.MyPurchaseOrder')),
                ('so', models.ForeignKey(to='erp.MySalesOrder')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MySalesOrderFullfillmentLineItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fullfill_qty', models.IntegerField(default=0)),
                ('po_line_item', models.ForeignKey(to='erp.MyPurchaseOrderLineItem')),
                ('so_fullfillment', models.ForeignKey(to='erp.MySalesOrderFullfillment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MySalesOrderLineItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('size', models.CharField(default=b'', max_length=4)),
                ('qty', models.IntegerField(default=0)),
                ('price', models.FloatField(default=0)),
                ('value', models.FloatField(default=0)),
                ('fullfilled', models.IntegerField(default=0)),
                ('fullfill_rate', models.FloatField(default=0)),
                ('item', models.ForeignKey(to='erp.MyItem')),
                ('order', models.ForeignKey(to='erp.MySalesOrder')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='myvendor',
            name='home_currency',
        ),
        migrations.AddField(
            model_name='mysalesorderfullfillmentlineitem',
            name='so_line_item',
            field=models.ForeignKey(to='erp.MySalesOrderLineItem'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mypurchaseorderlineitem',
            name='so_line_item',
            field=models.ForeignKey(to='erp.MySalesOrderLineItem'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mypurchaseorder',
            name='so',
            field=models.ForeignKey(to='erp.MySalesOrder'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mypurchaseorder',
            name='vendor',
            field=models.ForeignKey(to='erp.MyCRM'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='mycompany',
            name='price_over_std_cost',
        ),
        migrations.RemoveField(
            model_name='myitem',
            name='size',
        ),
        migrations.RemoveField(
            model_name='myitem',
            name='sku',
        ),
        migrations.RemoveField(
            model_name='mylocation',
            name='company',
        ),
        migrations.RemoveField(
            model_name='mylocation',
            name='description',
        ),
        migrations.RemoveField(
            model_name='mylocation',
            name='hash',
        ),
        migrations.RemoveField(
            model_name='mylocation',
            name='help_text',
        ),
        migrations.RemoveField(
            model_name='mylocation',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='mystorage',
            name='description',
        ),
        migrations.RemoveField(
            model_name='mystorage',
            name='hash',
        ),
        migrations.RemoveField(
            model_name='mystorage',
            name='help_text',
        ),
        migrations.RemoveField(
            model_name='mystorage',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='mystorage',
            name='name',
        ),
        migrations.AddField(
            model_name='myitem',
            name='order_deadline',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myiteminventory',
            name='size',
            field=models.CharField(default=b'', max_length=4),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myiteminventory',
            name='withdrawable',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mylocation',
            name='crm',
            field=models.ForeignKey(default=None, to='erp.MyCRM'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mylocation',
            name='name',
            field=models.CharField(default=None, max_length=32, verbose_name='\u540d\u79f0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mystorage',
            name='abbrev',
            field=models.CharField(max_length=32, null=True, verbose_name='Abbreviation', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myvendoritem',
            name='vendor',
            field=models.ForeignKey(to='erp.MyCRM'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='MyVendor',
        ),
    ]
