# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0015_auto_20160209_0943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myitem',
            name='SKU',
        ),
    ]
