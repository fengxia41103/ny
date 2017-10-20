# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0014_auto_20171020_0046'),
    ]

    operations = [
        migrations.CreateModel(
            name='MfgEndpointModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imm_ip', models.GenericIPAddressField(null=True, verbose_name='IMM IP4 address', blank=True)),
                ('imm_user', models.CharField(default=b'lenovo', max_length=32, null=True, verbose_name='IMM user', blank=True)),
                ('imm_password', models.CharField(default=b'passw0rd', max_length=32, null=True, verbose_name='IMM password', blank=True)),
                ('username', models.CharField(default=b'lxca', max_length=32, null=True, verbose_name='Mgt user', blank=True)),
                ('password', models.CharField(default=b'Th1nkAg!le', max_length=32, null=True, verbose_name='Mgt password', blank=True)),
                ('ip4', models.GenericIPAddressField(null=True, verbose_name='Mgt IP4 address', blank=True)),
                ('ip6', models.GenericIPAddressField(null=True, verbose_name='Mgt IP6 address', blank=True)),
                ('serial', models.CharField(max_length=64, null=True, verbose_name='Serial number', blank=True)),
                ('uuid', django_extensions.db.fields.UUIDField(default=uuid.uuid4, editable=False, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='orderendpointmodel',
            name='imm_ip',
        ),
        migrations.RemoveField(
            model_name='orderendpointmodel',
            name='imm_password',
        ),
        migrations.RemoveField(
            model_name='orderendpointmodel',
            name='imm_user',
        ),
        migrations.RemoveField(
            model_name='orderendpointmodel',
            name='ip4',
        ),
        migrations.RemoveField(
            model_name='orderendpointmodel',
            name='ip6',
        ),
        migrations.RemoveField(
            model_name='orderendpointmodel',
            name='password',
        ),
        migrations.RemoveField(
            model_name='orderendpointmodel',
            name='serial',
        ),
        migrations.RemoveField(
            model_name='orderendpointmodel',
            name='username',
        ),
        migrations.RemoveField(
            model_name='orderendpointmodel',
            name='uuid',
        ),
        migrations.AlterField(
            model_name='architectendpoint',
            name='playbooks',
            field=models.ManyToManyField(to='lxca.Playbook', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='architectsolution',
            name='applications',
            field=models.ManyToManyField(to='lxca.ArchitectApplication', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='architectsolution',
            name='playbooks',
            field=models.ManyToManyField(to='lxca.Playbook', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='architectsolution',
            name='powers',
            field=models.ManyToManyField(to='lxca.ArchitectPdu', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='architectsolution',
            name='racks',
            field=models.ManyToManyField(to='lxca.ArchitectRack', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='architectsolution',
            name='servers',
            field=models.ManyToManyField(to='lxca.ArchitectServer', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='architectsolution',
            name='switches',
            field=models.ManyToManyField(to='lxca.ArchitectSwitch', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='architectsolution',
            name='version',
            field=models.CharField(default=b'Alpha', max_length=8),
            preserve_default=True,
        ),
    ]
