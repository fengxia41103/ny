# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0008_auto_20171014_1743'),
    ]

    operations = [
        migrations.RenameField(
            model_name='architectrack',
            old_name='rack',
            new_name='catalog',
        ),
        migrations.RenameField(
            model_name='architectserver',
            old_name='server',
            new_name='catalog',
        ),
        migrations.RenameField(
            model_name='architectswitch',
            old_name='switch',
            new_name='catalog',
        ),
        migrations.RenameField(
            model_name='mfgrack',
            old_name='rack',
            new_name='on_order',
        ),
        migrations.RenameField(
            model_name='mfgserver',
            old_name='server',
            new_name='on_order',
        ),
        migrations.RenameField(
            model_name='mfgswitch',
            old_name='switch',
            new_name='on_order',
        ),
        migrations.RenameField(
            model_name='orderrack',
            old_name='rack',
            new_name='template',
        ),
        migrations.RenameField(
            model_name='orderserver',
            old_name='server',
            new_name='template',
        ),
        migrations.RenameField(
            model_name='orderswitch',
            old_name='switch',
            new_name='template',
        ),
    ]
