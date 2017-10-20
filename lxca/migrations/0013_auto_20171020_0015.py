# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0012_playbook_for_type'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='playbook',
            unique_together=set([]),
        ),
    ]
