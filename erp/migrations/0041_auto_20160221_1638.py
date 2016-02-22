# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0040_mysalesorderpayment'),
    ]

    operations = [
        migrations.AddField(
            model_name='mysalesorderpayment',
            name='useage',
            field=models.CharField(default=b'pay', max_length=32, choices=[(b'pay', b'Pay for a sales order'), (b'deposit', b'Deposit for a sales order')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mysalesorderpayment',
            name='created_by',
            field=models.ForeignKey(related_name='Logger', blank=True, to=settings.AUTH_USER_MODEL, help_text=b'', null=True, verbose_name='\u521b\u5efa\u7528\u6237'),
            preserve_default=True,
        ),
    ]
