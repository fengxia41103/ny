# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0006_auto_20171019_1935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mfgrack',
            name='bm_manager',
        ),
        migrations.RemoveField(
            model_name='mfgrack',
            name='on_order',
        ),
        migrations.RemoveField(
            model_name='mfgserver',
            name='bm_manager',
        ),
        migrations.RemoveField(
            model_name='mfgserver',
            name='on_order',
        ),
        migrations.RemoveField(
            model_name='mfgsolution',
            name='racks',
        ),
        migrations.DeleteModel(
            name='MfgRack',
        ),
        migrations.RemoveField(
            model_name='mfgsolution',
            name='servers',
        ),
        migrations.DeleteModel(
            name='MfgServer',
        ),
        migrations.RemoveField(
            model_name='mfgsolution',
            name='switches',
        ),
        migrations.DeleteModel(
            name='MfgSolution',
        ),
        migrations.RemoveField(
            model_name='mfgswitch',
            name='bm_manager',
        ),
        migrations.RemoveField(
            model_name='mfgswitch',
            name='on_order',
        ),
        migrations.DeleteModel(
            name='MfgSwitch',
        ),
        migrations.AddField(
            model_name='orderendpointmodel',
            name='serial',
            field=models.CharField(max_length=64, null=True, verbose_name='Serial number', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orderendpointmodel',
            name='uuid',
            field=django_extensions.db.fields.UUIDField(default=uuid.uuid4, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ordersolution',
            name='bm_manager',
            field=models.ForeignKey(blank=True, to='lxca.BaremetalManager', null=True),
            preserve_default=True,
        ),
    ]
