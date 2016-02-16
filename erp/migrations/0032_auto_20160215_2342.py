# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('erp', '0031_auto_20160215_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='mylocation',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myitem',
            name='size_chart',
            field=models.ForeignKey(blank=True, to='erp.MySizeChart', null=True),
            preserve_default=True,
        ),
    ]
