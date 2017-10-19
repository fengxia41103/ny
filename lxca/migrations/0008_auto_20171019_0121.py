# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0007_auto_20171018_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='architectbasemodel',
            name='firmware_repo',
        ),
        migrations.AddField(
            model_name='architectsolution',
            name='firmware_repo',
            field=models.ForeignKey(default=1, to='lxca.ArchitectFirmwareRepo'),
            preserve_default=False,
        ),
    ]
