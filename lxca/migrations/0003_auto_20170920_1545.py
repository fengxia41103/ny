# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0002_auto_20170919_2045'),
    ]

    operations = [
        migrations.CreateModel(
            name='PduConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bm_user', models.CharField(default=b'', max_length=64)),
                ('bm_password', models.CharField(default=b'', max_length=32)),
                ('bm_manager_url', models.URLField(default=b'')),
                ('imm_ip', models.GenericIPAddressField(null=True, blank=True)),
                ('imm_user', models.CharField(default=b'', max_length=64)),
                ('imm_password', models.CharField(default=b'', max_length=32)),
                ('firmware_update', models.CharField(default=b'', max_length=32)),
                ('config_pattern', models.CharField(default=b'', max_length=32)),
                ('pdu', models.ForeignKey(to='lxca.PDU')),
                ('playbooks', models.ManyToManyField(to='lxca.Playbook')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='solution',
            name='pdus',
        ),
        migrations.RemoveField(
            model_name='solution',
            name='racks',
        ),
        migrations.RemoveField(
            model_name='solution',
            name='servers',
        ),
        migrations.RemoveField(
            model_name='solution',
            name='storages',
        ),
        migrations.RemoveField(
            model_name='solution',
            name='switches',
        ),
        migrations.AddField(
            model_name='rackconfig',
            name='pdu_configs',
            field=models.ManyToManyField(to='lxca.PduConfig'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rackconfig',
            name='server_configs',
            field=models.ManyToManyField(to='lxca.ServerConfig'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rackconfig',
            name='storage_configs',
            field=models.ManyToManyField(to='lxca.StorageConfig'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rackconfig',
            name='switch_configs',
            field=models.ManyToManyField(to='lxca.SwitchConfig'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='solutionconfig',
            name='racks',
            field=models.ManyToManyField(to='lxca.RackConfig'),
            preserve_default=True,
        ),
    ]
