# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0017_auto_20160210_0853'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyItemInventoryAdjustment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inv', models.ForeignKey(to='erp.MyItemInventory')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='myiteminventory',
            name='withdrawable',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
