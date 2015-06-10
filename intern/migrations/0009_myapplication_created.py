# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0008_auto_20150609_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='myapplication',
            name='created',
            field=models.DateTimeField(default=None, auto_now_add=True),
            preserve_default=False,
        ),
    ]
