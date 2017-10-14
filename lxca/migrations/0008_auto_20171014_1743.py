# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0007_auto_20171014_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderserver',
            name='ip',
            field=models.GenericIPAddressField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
