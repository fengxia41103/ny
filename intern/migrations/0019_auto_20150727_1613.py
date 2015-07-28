# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0018_auto_20150727_1540'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myitem',
            old_name='fate',
            new_name='status',
        ),
    ]
