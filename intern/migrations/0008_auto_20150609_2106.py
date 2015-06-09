# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0007_auto_20150609_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mystatusaudit',
            name='contact',
            field=models.ForeignKey(verbose_name='Contact person', to='intern.MyExternalContact'),
            preserve_default=True,
        ),
    ]
