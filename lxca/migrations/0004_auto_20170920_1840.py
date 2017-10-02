# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0003_auto_20170920_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rack',
            name='firmware',
        ),
        migrations.RemoveField(
            model_name='solution',
            name='firmware',
        ),
    ]
