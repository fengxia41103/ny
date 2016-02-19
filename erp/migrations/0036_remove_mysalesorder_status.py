# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0035_mylocation_abbrev'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mysalesorder',
            name='status',
        ),
    ]
