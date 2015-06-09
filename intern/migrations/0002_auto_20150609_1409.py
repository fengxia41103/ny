# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myapplication',
            name='description',
        ),
        migrations.RemoveField(
            model_name='myapplication',
            name='hash',
        ),
        migrations.RemoveField(
            model_name='myapplication',
            name='help_text',
        ),
        migrations.RemoveField(
            model_name='myapplication',
            name='name',
        ),
    ]
