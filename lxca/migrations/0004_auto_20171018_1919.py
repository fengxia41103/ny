# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0003_auto_20171018_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='architectfirmwarepolicy',
            name='repo',
        ),
        migrations.AddField(
            model_name='architectbasemodel',
            name='firmware_repo',
            field=models.ForeignKey(default=1, to='lxca.ArchitectFirmwareRepo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='architectbasemodel',
            name='firmware_policy',
            field=models.CharField(default=b'', max_length=32),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='ArchitectFirmwarePolicy',
        ),
    ]
