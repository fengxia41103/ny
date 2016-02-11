# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('erp', '0021_auto_20160210_1744'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyItemInventoryMoveAudit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('out', models.BooleanField(default=False)),
                ('qty', models.IntegerField(default=0)),
                ('reason', models.TextField(default=b'')),
                ('created_by', models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL, blank=True, help_text=b'', null=True, verbose_name='\u521b\u5efa\u7528\u6237')),
                ('inv', models.ForeignKey(to='erp.MyItemInventory')),
                ('so', models.ForeignKey(blank=True, to='erp.MySalesOrderFullfillment', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='myiteminventoryaudit',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='myiteminventoryaudit',
            name='inv',
        ),
        migrations.RemoveField(
            model_name='myiteminventoryaudit',
            name='so',
        ),
        migrations.DeleteModel(
            name='MyItemInventoryAudit',
        ),
    ]
