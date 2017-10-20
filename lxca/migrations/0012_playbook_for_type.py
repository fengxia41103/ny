# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0011_playbook_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='playbook',
            name='for_type',
            field=models.IntegerField(default=5, null=True, blank=True, choices=[(1, 'Solution'), (2, 'Rack'), (3, 'PDU'), (4, 'Switch'), (5, 'Server')]),
            preserve_default=True,
        ),
    ]
