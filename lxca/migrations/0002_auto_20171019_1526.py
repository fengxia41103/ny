# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalogpdu',
            name='inputs',
        ),
        migrations.AddField(
            model_name='catalogpdu',
            name='input',
            field=models.ForeignKey(default=1, to='lxca.PduInput'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='pduinput',
            unique_together=set([('phase', 'frequency')]),
        ),
        migrations.RemoveField(
            model_name='pduinput',
            name='voltage',
        ),
        migrations.RemoveField(
            model_name='pduinput',
            name='current',
        ),
        migrations.AlterUniqueTogether(
            name='pduoutput',
            unique_together=set([('voltage', 'power_limit_per_pdu', 'power_limit_per_outlet', 'power_limit_per_group')]),
        ),
        migrations.RemoveField(
            model_name='pduoutput',
            name='capacity',
        ),
    ]
