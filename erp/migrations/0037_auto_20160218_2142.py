# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0036_remove_mysalesorder_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyBusinessModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hash', models.CharField(default=b'', max_length=256, null=True, verbose_name='MD5 hash', blank=True)),
                ('name', models.CharField(default=None, max_length=128, verbose_name='\u540d\u79f0')),
                ('description', models.TextField(null=True, verbose_name='\u63cf\u8ff0', blank=True)),
                ('abbrev', models.CharField(max_length=8, null=True, verbose_name='Abbreviation', blank=True)),
                ('help_text', models.CharField(max_length=64, null=True, verbose_name='\u5e2e\u52a9\u63d0\u793a', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('sales_model', models.CharField(default=b'Retail', max_length=64, choices=[(b'Retail', b'Retail'), (b'Wholesale', b'Wholesale'), (b'Consignment', b'Consignment'), (b'Leasing', b'Leasing')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='mysalesorder',
            name='business_model',
            field=models.ForeignKey(default=1, to='erp.MyBusinessModel'),
            preserve_default=False,
        ),
    ]
