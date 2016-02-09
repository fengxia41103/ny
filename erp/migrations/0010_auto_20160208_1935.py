# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0009_auto_20160208_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyStorage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hash', models.CharField(default=b'', max_length=256, null=True, verbose_name='MD5 hash', blank=True)),
                ('name', models.CharField(default=None, max_length=128, verbose_name='\u540d\u79f0')),
                ('description', models.TextField(null=True, verbose_name='\u63cf\u8ff0', blank=True)),
                ('abbrev', models.CharField(max_length=8, null=True, verbose_name='Abbreviation', blank=True)),
                ('help_text', models.CharField(max_length=64, null=True, verbose_name='\u5e2e\u52a9\u63d0\u793a', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('location', models.ForeignKey(to='erp.MyLocation')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='mywarehouse',
            name='location',
        ),
        migrations.RemoveField(
            model_name='myiteminventory',
            name='locations',
        ),
        migrations.RemoveField(
            model_name='myiteminventory',
            name='warehouses',
        ),
        migrations.DeleteModel(
            name='MyWarehouse',
        ),
        migrations.AddField(
            model_name='myiteminventory',
            name='storage',
            field=models.ForeignKey(default=None, to='erp.MyStorage'),
            preserve_default=False,
        ),
    ]
