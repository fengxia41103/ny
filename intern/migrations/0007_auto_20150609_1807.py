# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0006_auto_20150609_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mystatusaudit',
            name='status',
        ),
        migrations.AddField(
            model_name='mystatusaudit',
            name='new_status',
            field=models.CharField(default=b'', max_length=64, verbose_name='New status'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mystatusaudit',
            name='old_status',
            field=models.CharField(default=b'', max_length=64, verbose_name='Old status'),
            preserve_default=True,
        ),
    ]
