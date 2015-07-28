# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0017_auto_20150727_1522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myitem',
            old_name='box',
            new_name='boxes',
        ),
        migrations.RenameField(
            model_name='myitem',
            old_name='room',
            new_name='rooms',
        ),
    ]
