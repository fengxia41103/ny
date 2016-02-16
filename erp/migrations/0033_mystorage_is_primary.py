# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0032_auto_20160215_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='mystorage',
            name='is_primary',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
