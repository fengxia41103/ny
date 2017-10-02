# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0006_auto_20170930_1814'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('host', models.CharField(max_length=32, choices=[(b'win210svr', b'Windows Server 2010'), (b'esxi', b'ESXI server'), (b'Ubuntu xeniel', b'Ubuntu 16.04 Xeniel'), (b'Ubuntu trusty', b'Ubuntu 14.04 Trusty')])),
                ('compatible_servers', models.ManyToManyField(to='lxca.Server')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderServerModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firmware', models.CharField(default=b'firmware version', max_length=32)),
                ('cores', models.IntegerField(default=2)),
                ('mem', models.IntegerField(default=16, help_text='Memory size in GB')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StorageDisk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('physical_format', models.CharField(default=b'2.5', max_length=8, choices=[(b'2.5', b'2.5 inch'), (b'3.5', b'3.5 inch'), (b'ssd', b'ssd')])),
                ('capacity_in_gb', models.IntegerField(default=100, help_text='Storage capacity in GB.')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='server',
            old_name='cores',
            new_name='cpu_sockets',
        ),
        migrations.RemoveField(
            model_name='pdu',
            name='firmware',
        ),
        migrations.RemoveField(
            model_name='raidadapter',
            name='firmware',
        ),
        migrations.RemoveField(
            model_name='server',
            name='firmware',
        ),
        migrations.RemoveField(
            model_name='server',
            name='mem',
        ),
        migrations.RemoveField(
            model_name='switch',
            name='firmware',
        ),
        migrations.AddField(
            model_name='server',
            name='max_25_disk',
            field=models.IntegerField(default=12),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='server',
            name='max_35_disk',
            field=models.IntegerField(default=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='storageconfig',
            name='storage',
            field=models.ForeignKey(to='lxca.StorageDisk'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Storage',
        ),
    ]
