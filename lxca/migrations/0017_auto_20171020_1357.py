# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0016_auto_20171020_0154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mfgpdu',
            old_name='solution',
            new_name='mfg',
        ),
        migrations.RenameField(
            model_name='mfgrack',
            old_name='solution',
            new_name='mfg',
        ),
        migrations.RenameField(
            model_name='mfgserver',
            old_name='solution',
            new_name='mfg',
        ),
        migrations.RenameField(
            model_name='mfgswitch',
            old_name='solution',
            new_name='mfg',
        ),
    ]
