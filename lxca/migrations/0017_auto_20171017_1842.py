# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0016_auto_20171017_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogpdu',
            name='c13',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='catalogpdu',
            name='c19',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
