# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0008_auto_20160208_1905'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mywarehouse',
            old_name='company',
            new_name='location',
        ),
    ]
