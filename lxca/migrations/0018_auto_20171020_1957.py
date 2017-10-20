# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0017_auto_20171020_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='baremetalmanager',
            name='recovery_id',
            field=models.CharField(default=b'root', max_length=32),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='baremetalmanager',
            name='recovery_password',
            field=models.CharField(default=b'Passw0rd', max_length=32),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='orderserver',
            name='storages',
            field=models.ManyToManyField(to='lxca.CatalogStorageDisk', blank=True),
            preserve_default=True,
        ),
    ]
