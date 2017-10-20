# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0013_auto_20171020_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='architectsolution',
            name='applications',
            field=models.ManyToManyField(to='lxca.ArchitectApplication', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='architectsolution',
            name='compliance',
            field=models.ForeignKey(default=1, to='lxca.ArchitectCompliance'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='architectsolution',
            name='firmware_repo',
            field=models.ForeignKey(default=1, to='lxca.ArchitectFirmwareRepo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='architectsolution',
            name='lxca',
            field=models.ForeignKey(default=1, to='lxca.ArchitectLxca'),
            preserve_default=True,
        ),
    ]
