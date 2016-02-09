# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0011_auto_20160208_2113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mycurrency',
            name='hundredths',
        ),
    ]
