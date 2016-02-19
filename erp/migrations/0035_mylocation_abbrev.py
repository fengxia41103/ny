# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0034_auto_20160216_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='mylocation',
            name='abbrev',
            field=models.CharField(max_length=5, null=True, blank=True),
            preserve_default=True,
        ),
    ]
