# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='architectfirmwarerepo',
            old_name='firmware_fix_id',
            new_name='fix_id',
        ),
        migrations.RemoveField(
            model_name='architectfirmwarerepo',
            name='firmware_pack',
        ),
        migrations.RemoveField(
            model_name='architectfirmwarerepo',
            name='update_access_location',
        ),
        migrations.AddField(
            model_name='architectfirmwarerepo',
            name='pack_filename',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='architectfirmwarerepo',
            name='update_access_method',
            field=models.CharField(default=b'm', max_length=1, choices=[(b'm', b'manual')]),
            preserve_default=True,
        ),
    ]
