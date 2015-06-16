# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0012_mysponsor_is_return_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mysponsor',
            name='is_return_balance',
        ),
        migrations.AddField(
            model_name='mysponsor',
            name='is_sas_paying_student_fees',
            field=models.BooleanField(default=False, verbose_name='Does SAS pay student fees?'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mysponsor',
            name='is_to_return_balance',
            field=models.BooleanField(default=False, verbose_name='Need to return remaining balance?'),
            preserve_default=True,
        ),
    ]
