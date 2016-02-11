# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0019_auto_20160210_0949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myiteminventoryaudit',
            name='reason',
        ),
        migrations.AddField(
            model_name='myiteminventoryaudit',
            name='note',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
