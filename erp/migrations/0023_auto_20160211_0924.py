# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0022_auto_20160211_0850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mysalesorder',
            name='supplier',
        ),
        migrations.AlterField(
            model_name='mysalesorder',
            name='customer',
            field=models.ForeignKey(to='erp.MyCRM'),
            preserve_default=True,
        ),
    ]
