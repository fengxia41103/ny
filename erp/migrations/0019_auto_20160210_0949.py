# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('erp', '0018_auto_20160210_0901'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyItemInventoryAudit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('out', models.BooleanField(default=False)),
                ('qty', models.IntegerField(default=0)),
                ('reason', models.CharField(max_length=8, choices=[(b'SO', b'Qty is being adjusted due to fullfillment of a sales order.'), (b'INITIAL', b'Qty is being adjusted as an initial setup.'), (b'DAMAGE', b'Qty is being adjusted due to a damaged goods.')])),
                ('created_by', models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL, blank=True, help_text=b'', null=True, verbose_name='\u521b\u5efa\u7528\u6237')),
                ('inv', models.ForeignKey(to='erp.MyItemInventory')),
                ('so', models.ForeignKey(blank=True, to='erp.MySalesOrderFullfillment', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='myiteminventoryadjustment',
            name='inv',
        ),
        migrations.DeleteModel(
            name='MyItemInventoryAdjustment',
        ),
        migrations.RenameField(
            model_name='myiteminventory',
            old_name='qty',
            new_name='physical',
        ),
        migrations.AddField(
            model_name='mysalesorder',
            name='supplier',
            field=models.ForeignKey(related_name='supplier', default=None, to='erp.MyCRM'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mysalesorder',
            name='customer',
            field=models.ForeignKey(related_name='customer', to='erp.MyCRM'),
            preserve_default=True,
        ),
    ]
