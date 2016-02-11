# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('erp', '0023_auto_20160211_0924'),
    ]

    operations = [
        migrations.AddField(
            model_name='mysalesorder',
            name='sales',
            field=models.ForeignKey(related_name='sales', default=None, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mysalesorder',
            name='created_by',
            field=models.ForeignKey(related_name='logger', default=None, to=settings.AUTH_USER_MODEL, blank=True, help_text=b'', null=True, verbose_name='\u521b\u5efa\u7528\u6237'),
            preserve_default=True,
        ),
    ]
