# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0016_remove_myitem_sku'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mylocation',
            name='abbrev',
        ),
        migrations.RemoveField(
            model_name='mystorage',
            name='abbrev',
        ),
    ]
