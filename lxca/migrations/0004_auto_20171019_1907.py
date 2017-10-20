# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0003_auto_20171019_1850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mfgrack',
            name='config_pattern',
        ),
        migrations.RemoveField(
            model_name='mfgrack',
            name='firmware_update',
        ),
        migrations.RemoveField(
            model_name='mfgrack',
            name='imm_ip',
        ),
        migrations.RemoveField(
            model_name='mfgrack',
            name='imm_password',
        ),
        migrations.RemoveField(
            model_name='mfgrack',
            name='imm_user',
        ),
        migrations.RemoveField(
            model_name='mfgrack',
            name='mtm',
        ),
        migrations.RemoveField(
            model_name='mfgrack',
            name='uuid',
        ),
        migrations.RemoveField(
            model_name='mfgserver',
            name='config_pattern',
        ),
        migrations.RemoveField(
            model_name='mfgserver',
            name='firmware_update',
        ),
        migrations.RemoveField(
            model_name='mfgserver',
            name='imm_ip',
        ),
        migrations.RemoveField(
            model_name='mfgserver',
            name='imm_password',
        ),
        migrations.RemoveField(
            model_name='mfgserver',
            name='imm_user',
        ),
        migrations.RemoveField(
            model_name='mfgserver',
            name='mtm',
        ),
        migrations.RemoveField(
            model_name='mfgserver',
            name='uuid',
        ),
        migrations.RemoveField(
            model_name='mfgswitch',
            name='config_pattern',
        ),
        migrations.RemoveField(
            model_name='mfgswitch',
            name='firmware_update',
        ),
        migrations.RemoveField(
            model_name='mfgswitch',
            name='imm_ip',
        ),
        migrations.RemoveField(
            model_name='mfgswitch',
            name='imm_password',
        ),
        migrations.RemoveField(
            model_name='mfgswitch',
            name='imm_user',
        ),
        migrations.RemoveField(
            model_name='mfgswitch',
            name='mtm',
        ),
        migrations.RemoveField(
            model_name='mfgswitch',
            name='uuid',
        ),
        migrations.RemoveField(
            model_name='orderserver',
            name='ip',
        ),
        migrations.AddField(
            model_name='orderendpointmodel',
            name='imm_ip',
            field=models.GenericIPAddressField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orderendpointmodel',
            name='imm_password',
            field=models.CharField(default=b'', max_length=32),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orderendpointmodel',
            name='imm_user',
            field=models.CharField(default=b'', max_length=64),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orderendpointmodel',
            name='ip4',
            field=models.GenericIPAddressField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orderendpointmodel',
            name='ip6',
            field=models.GenericIPAddressField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orderendpointmodel',
            name='password',
            field=models.CharField(default=b'Th1nkAg!le', max_length=32),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orderendpointmodel',
            name='username',
            field=models.CharField(default=b'mgr', max_length=32),
            preserve_default=True,
        ),
    ]
