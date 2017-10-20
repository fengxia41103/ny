# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0019_auto_20171020_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='architectsolution',
            name='uuid',
            field=django_extensions.db.fields.UUIDField(default=uuid.uuid4, editable=False, blank=True),
            preserve_default=True,
        ),
    ]
