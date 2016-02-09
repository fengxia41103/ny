# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hash', models.CharField(default=b'', max_length=256, null=True, verbose_name='MD5 hash', blank=True)),
                ('name', models.CharField(default=None, max_length=128, verbose_name='\u540d\u79f0')),
                ('description', models.TextField(null=True, verbose_name='\u63cf\u8ff0', blank=True)),
                ('abbrev', models.CharField(max_length=8, null=True, verbose_name='Abbreviation', blank=True)),
                ('help_text', models.CharField(max_length=64, null=True, verbose_name='\u5e2e\u52a9\u63d0\u793a', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('address', models.TextField()),
                ('company', models.ForeignKey(to='erp.MyCompany')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MyVendor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hash', models.CharField(default=b'', max_length=256, null=True, verbose_name='MD5 hash', blank=True)),
                ('name', models.CharField(default=None, max_length=128, verbose_name='\u540d\u79f0')),
                ('description', models.TextField(null=True, verbose_name='\u63cf\u8ff0', blank=True)),
                ('abbrev', models.CharField(max_length=8, null=True, verbose_name='Abbreviation', blank=True)),
                ('help_text', models.CharField(max_length=64, null=True, verbose_name='\u5e2e\u52a9\u63d0\u793a', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('contact', models.CharField(max_length=32, null=True, verbose_name='Vendor contact', blank=True)),
                ('phone', models.CharField(max_length=16, null=True, verbose_name='Vendor phone', blank=True)),
                ('balance', models.FloatField(default=0)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MyWarehouse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hash', models.CharField(default=b'', max_length=256, null=True, verbose_name='MD5 hash', blank=True)),
                ('name', models.CharField(default=None, max_length=128, verbose_name='\u540d\u79f0')),
                ('description', models.TextField(null=True, verbose_name='\u63cf\u8ff0', blank=True)),
                ('abbrev', models.CharField(max_length=8, null=True, verbose_name='Abbreviation', blank=True)),
                ('help_text', models.CharField(max_length=64, null=True, verbose_name='\u5e2e\u52a9\u63d0\u793a', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('address', models.TextField()),
                ('company', models.ForeignKey(to='erp.MyCompany')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='myitem',
            old_name='user_defined_code',
            new_name='sku',
        ),
        migrations.RemoveField(
            model_name='myitem',
            name='ean_code',
        ),
        migrations.RemoveField(
            model_name='myitem',
            name='upc_code',
        ),
        migrations.AddField(
            model_name='myitem',
            name='color',
            field=models.CharField(default=b'', max_length=32),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myitem',
            name='locations',
            field=models.ManyToManyField(to='erp.MyLocation'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myitem',
            name='size',
            field=models.CharField(default=b'', max_length=4),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myitem',
            name='vendors',
            field=models.ManyToManyField(to='erp.MyVendor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myitem',
            name='warehouses',
            field=models.ManyToManyField(to='erp.MyWarehouse'),
            preserve_default=True,
        ),
    ]
