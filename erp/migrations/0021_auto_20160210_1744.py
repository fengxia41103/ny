# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0020_auto_20160210_1736'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myiteminventoryaudit',
            old_name='note',
            new_name='reason',
        ),
    ]
