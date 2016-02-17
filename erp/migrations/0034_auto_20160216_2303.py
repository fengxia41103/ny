# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0033_mystorage_is_primary'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycrm',
            name='url',
            field=models.URLField(default=b'', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mylocation',
            name='address',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
