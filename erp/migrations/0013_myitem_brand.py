# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0012_remove_mycurrency_hundredths'),
    ]

    operations = [
        migrations.AddField(
            model_name='myitem',
            name='brand',
            field=models.ForeignKey(default=None, to='erp.MyCRM'),
            preserve_default=False,
        ),
    ]
