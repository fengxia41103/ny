# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0002_auto_20171014_1512'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rack',
            old_name='size',
            new_name='eia_capacity',
        ),
        migrations.RemoveField(
            model_name='rack',
            name='width',
        ),
        migrations.AddField(
            model_name='rack',
            name='expansion_racks',
            field=models.ForeignKey(default=None, to='lxca.Rack'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rack',
            name='sizewall_compartment',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mfgrack',
            name='mtm',
            field=models.CharField(default=b'', help_text=b'Machine type model', max_length=64),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mfgserver',
            name='mtm',
            field=models.CharField(default=b'', help_text=b'Machine type model', max_length=64),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mfgswitch',
            name='mtm',
            field=models.CharField(default=b'', help_text=b'Machine type model', max_length=64),
            preserve_default=True,
        ),
    ]
