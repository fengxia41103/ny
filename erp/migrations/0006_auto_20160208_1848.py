# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0005_auto_20151209_0645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myitem',
            name='sources',
        ),
        migrations.AddField(
            model_name='myvendoritem',
            name='currency',
            field=models.ForeignKey(default=None, to='erp.MyCurrency'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myvendoritem',
            name='product',
            field=models.ForeignKey(default=None, to='erp.MyItem'),
            preserve_default=False,
        ),
    ]
