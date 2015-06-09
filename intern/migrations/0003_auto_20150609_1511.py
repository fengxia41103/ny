# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0002_auto_20150609_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myapplication',
            name='comments',
            field=models.ManyToManyField(related_name='applications', null=True, verbose_name='Comments', to='intern.MyApplicationComment', blank=True),
            preserve_default=True,
        ),
    ]
