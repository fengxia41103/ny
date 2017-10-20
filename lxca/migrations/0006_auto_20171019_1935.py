# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0005_auto_20171019_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='mfgrack',
            name='uuid',
            field=django_extensions.db.fields.UUIDField(default=uuid.uuid4, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mfgserver',
            name='uuid',
            field=django_extensions.db.fields.UUIDField(default=uuid.uuid4, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mfgswitch',
            name='uuid',
            field=django_extensions.db.fields.UUIDField(default=uuid.uuid4, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='orderendpointmodel',
            name='imm_password',
            field=models.CharField(default=b'passw0rd', max_length=32, null=True, verbose_name='IMM password', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='orderendpointmodel',
            name='imm_user',
            field=models.CharField(default=b'lenovo', max_length=32, null=True, verbose_name='IMM user', blank=True),
            preserve_default=True,
        ),
    ]
