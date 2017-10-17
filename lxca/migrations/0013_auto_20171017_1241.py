# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0012_auto_20171016_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogpdu',
            name='size',
            field=models.IntegerField(default=1, choices=[(0, '0U'), (1, '1U'), (2, '2U')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='catalogpdu',
            name='voltage',
            field=models.CharField(default='120-1', max_length=16, choices=[('120-1', '120V single phase'), ('208-1', '208V single phase'), ('208-3', '208V three phase'), ('400-3', '400V three phase')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='catalograidadapter',
            name='size',
            field=models.IntegerField(default=1, choices=[(0, '0U'), (1, '1U'), (2, '2U')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='catalogserver',
            name='size',
            field=models.IntegerField(default=1, choices=[(0, '0U'), (1, '1U'), (2, '2U')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='catalogswitch',
            name='size',
            field=models.IntegerField(default=1, choices=[(0, '0U'), (1, '1U'), (2, '2U')]),
            preserve_default=True,
        ),
    ]
