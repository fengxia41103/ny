# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0008_auto_20171019_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderendpointmodel',
            name='imm_ip',
            field=models.GenericIPAddressField(null=True, verbose_name='IMM IP4 address', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='orderendpointmodel',
            name='ip4',
            field=models.GenericIPAddressField(null=True, verbose_name='Mgt IP4 address', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='orderendpointmodel',
            name='ip6',
            field=models.GenericIPAddressField(null=True, verbose_name='Mgt IP6 address', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='orderendpointmodel',
            name='password',
            field=models.CharField(default=b'Th1nkAg!le', max_length=32, null=True, verbose_name='Mgt password', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='orderendpointmodel',
            name='username',
            field=models.CharField(default=b'lxca', max_length=32, null=True, verbose_name='Mgt user', blank=True),
            preserve_default=True,
        ),
    ]
