# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0027_auto_20160211_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='mysalesorder',
            name='status',
            field=models.CharField(default=b'N', max_length=16, null=True, blank=True, choices=[(b'N', b'New'), (b'C', b'Closed'), (b'R', b'In Review'), (b'F', b'Fullfilling')]),
            preserve_default=True,
        ),
    ]
