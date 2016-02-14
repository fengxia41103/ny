# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0029_auto_20160212_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='mysalesorder',
            name='default_storage',
            field=models.ForeignKey(blank=True, to='erp.MyStorage', null=True),
            preserve_default=True,
        ),
    ]
