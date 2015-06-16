# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0011_auto_20150611_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='mysponsor',
            name='is_return_balance',
            field=models.BooleanField(default=False, verbose_name='To return remaining balance'),
            preserve_default=True,
        ),
    ]
