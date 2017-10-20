# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0015_auto_20171020_0140'),
    ]

    operations = [
        migrations.CreateModel(
            name='MfgPdu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('serial', models.CharField(max_length=64, null=True, verbose_name='Serial number', blank=True)),
                ('uuid', django_extensions.db.fields.UUIDField(default=uuid.uuid4, editable=False, blank=True)),
                ('imm_ip', models.GenericIPAddressField(null=True, verbose_name='IMM IP4 address', blank=True)),
                ('imm_user', models.CharField(default=b'lenovo', max_length=32, null=True, verbose_name='IMM user', blank=True)),
                ('imm_password', models.CharField(default=b'passw0rd', max_length=32, null=True, verbose_name='IMM password', blank=True)),
                ('username', models.CharField(default=b'lxca', max_length=32, null=True, verbose_name='Mgt user', blank=True)),
                ('password', models.CharField(default=b'Th1nkAg!le', max_length=32, null=True, verbose_name='Mgt password', blank=True)),
                ('ip4', models.GenericIPAddressField(null=True, verbose_name='Mgt IP4 address', blank=True)),
                ('ip6', models.GenericIPAddressField(null=True, verbose_name='Mgt IP6 address', blank=True)),
                ('order', models.ForeignKey(to='lxca.OrderPdu')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MfgRack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('serial', models.CharField(max_length=64, null=True, verbose_name='Serial number', blank=True)),
                ('uuid', django_extensions.db.fields.UUIDField(default=uuid.uuid4, editable=False, blank=True)),
                ('imm_ip', models.GenericIPAddressField(null=True, verbose_name='IMM IP4 address', blank=True)),
                ('imm_user', models.CharField(default=b'lenovo', max_length=32, null=True, verbose_name='IMM user', blank=True)),
                ('imm_password', models.CharField(default=b'passw0rd', max_length=32, null=True, verbose_name='IMM password', blank=True)),
                ('username', models.CharField(default=b'lxca', max_length=32, null=True, verbose_name='Mgt user', blank=True)),
                ('password', models.CharField(default=b'Th1nkAg!le', max_length=32, null=True, verbose_name='Mgt password', blank=True)),
                ('ip4', models.GenericIPAddressField(null=True, verbose_name='Mgt IP4 address', blank=True)),
                ('ip6', models.GenericIPAddressField(null=True, verbose_name='Mgt IP6 address', blank=True)),
                ('order', models.ForeignKey(to='lxca.OrderRack')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MfgServer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('serial', models.CharField(max_length=64, null=True, verbose_name='Serial number', blank=True)),
                ('uuid', django_extensions.db.fields.UUIDField(default=uuid.uuid4, editable=False, blank=True)),
                ('imm_ip', models.GenericIPAddressField(null=True, verbose_name='IMM IP4 address', blank=True)),
                ('imm_user', models.CharField(default=b'lenovo', max_length=32, null=True, verbose_name='IMM user', blank=True)),
                ('imm_password', models.CharField(default=b'passw0rd', max_length=32, null=True, verbose_name='IMM password', blank=True)),
                ('username', models.CharField(default=b'lxca', max_length=32, null=True, verbose_name='Mgt user', blank=True)),
                ('password', models.CharField(default=b'Th1nkAg!le', max_length=32, null=True, verbose_name='Mgt password', blank=True)),
                ('ip4', models.GenericIPAddressField(null=True, verbose_name='Mgt IP4 address', blank=True)),
                ('ip6', models.GenericIPAddressField(null=True, verbose_name='Mgt IP6 address', blank=True)),
                ('order', models.ForeignKey(to='lxca.OrderServer')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MfgSolution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bm_manager', models.ForeignKey(blank=True, to='lxca.BaremetalManager', null=True)),
                ('order', models.ForeignKey(to='lxca.OrderSolution')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MfgSwitch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('serial', models.CharField(max_length=64, null=True, verbose_name='Serial number', blank=True)),
                ('uuid', django_extensions.db.fields.UUIDField(default=uuid.uuid4, editable=False, blank=True)),
                ('imm_ip', models.GenericIPAddressField(null=True, verbose_name='IMM IP4 address', blank=True)),
                ('imm_user', models.CharField(default=b'lenovo', max_length=32, null=True, verbose_name='IMM user', blank=True)),
                ('imm_password', models.CharField(default=b'passw0rd', max_length=32, null=True, verbose_name='IMM password', blank=True)),
                ('username', models.CharField(default=b'lxca', max_length=32, null=True, verbose_name='Mgt user', blank=True)),
                ('password', models.CharField(default=b'Th1nkAg!le', max_length=32, null=True, verbose_name='Mgt password', blank=True)),
                ('ip4', models.GenericIPAddressField(null=True, verbose_name='Mgt IP4 address', blank=True)),
                ('ip6', models.GenericIPAddressField(null=True, verbose_name='Mgt IP6 address', blank=True)),
                ('order', models.ForeignKey(to='lxca.OrderSwitch')),
                ('solution', models.ForeignKey(to='lxca.MfgSolution')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='MfgEndpointModel',
        ),
        migrations.AddField(
            model_name='mfgserver',
            name='solution',
            field=models.ForeignKey(to='lxca.MfgSolution'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mfgrack',
            name='solution',
            field=models.ForeignKey(to='lxca.MfgSolution'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mfgpdu',
            name='solution',
            field=models.ForeignKey(to='lxca.MfgSolution'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='ordersolution',
            name='bm_manager',
        ),
    ]
