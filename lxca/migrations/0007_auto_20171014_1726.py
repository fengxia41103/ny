# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0006_auto_20171014_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogPdu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='default name', max_length=128)),
                ('description', models.TextField(default=b'')),
                ('help_text', models.CharField(max_length=64, null=True, verbose_name='Help', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('size', models.CharField(default='1U', max_length=8, choices=[('1U', '1U'), ('2U', '2U')])),
                ('orientation', models.CharField(default='h', max_length=16, choices=[('h', 'Horizontal'), ('v', 'Vertical')])),
                ('voltage', models.CharField(default='120-1', max_length=16, choices=[('120-1', '120V single phase'), ('208-1', '208V single phase'), ('120-3', '208V three phase'), ('400-3', '400V three phase')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CatalogRack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='default name', max_length=128)),
                ('description', models.TextField(default=b'')),
                ('help_text', models.CharField(max_length=64, null=True, verbose_name='Help', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_primary', models.BooleanField(default=True, verbose_name='Is primary rack')),
                ('eia_capacity', models.IntegerField(default=25, choices=[(25, '25U'), (42, '42U')])),
                ('sizewall_compartment', models.IntegerField(default=0)),
                ('expansion_racks', models.ForeignKey(default=None, blank=True, to='lxca.CatalogRack', help_text=b'Expansion rack for the primary', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CatalogRaidAdapter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='default name', max_length=128)),
                ('description', models.TextField(default=b'')),
                ('help_text', models.CharField(max_length=64, null=True, verbose_name='Help', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('size', models.CharField(default='1U', max_length=8, choices=[('1U', '1U'), ('2U', '2U')])),
                ('orientation', models.CharField(default='h', max_length=16, choices=[('h', 'Horizontal'), ('v', 'Vertical')])),
                ('speed', models.IntegerField(default=1, verbose_name='PCI speed', choices=[(1, b'PCIx1'), (4, b'PCIx4'), (6, b'PCIx6')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CatalogServer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='default name', max_length=128)),
                ('description', models.TextField(default=b'')),
                ('help_text', models.CharField(max_length=64, null=True, verbose_name='Help', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('size', models.CharField(default='1U', max_length=8, choices=[('1U', '1U'), ('2U', '2U')])),
                ('orientation', models.CharField(default='h', max_length=16, choices=[('h', 'Horizontal'), ('v', 'Vertical')])),
                ('cpu_sockets', models.IntegerField(default=2)),
                ('max_25_disk', models.IntegerField(default=12)),
                ('max_35_disk', models.IntegerField(default=10)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CatalogSwitch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='default name', max_length=128)),
                ('description', models.TextField(default=b'')),
                ('help_text', models.CharField(max_length=64, null=True, verbose_name='Help', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('size', models.CharField(default='1U', max_length=8, choices=[('1U', '1U'), ('2U', '2U')])),
                ('orientation', models.CharField(default='h', max_length=16, choices=[('h', 'Horizontal'), ('v', 'Vertical')])),
                ('speed', models.IntegerField(default=10, choices=[(1, '1G'), (10, '10G')])),
                ('rear_to_front', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MyOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.CharField(default=b'21873', help_text='Order number', max_length=32)),
                ('status', models.IntegerField(default=1, choices=[(1, 'draft'), (2, 'in MFG'), (3, 'in provisioning'), (4, 'in deployment'), (5, 'obsolete')])),
                ('solution', models.ForeignKey(to='lxca.ArchitectSolution')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='StorageDisk',
            new_name='CatalogStorageDisk',
        ),
        migrations.RemoveField(
            model_name='ordersolution',
            name='racks',
        ),
        migrations.RemoveField(
            model_name='ordersolution',
            name='servers',
        ),
        migrations.RemoveField(
            model_name='ordersolution',
            name='solution',
        ),
        migrations.RemoveField(
            model_name='ordersolution',
            name='switches',
        ),
        migrations.DeleteModel(
            name='OrderSolution',
        ),
        migrations.DeleteModel(
            name='PDU',
        ),
        migrations.RemoveField(
            model_name='rack',
            name='expansion_racks',
        ),
        migrations.DeleteModel(
            name='RaidAdapter',
        ),
        migrations.RemoveField(
            model_name='architectsolution',
            name='manifestversion_major',
        ),
        migrations.RemoveField(
            model_name='architectsolution',
            name='manifestversion_minor',
        ),
        migrations.AddField(
            model_name='architectsolution',
            name='version',
            field=models.CharField(default='0.1', max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderbasemodel',
            name='order',
            field=models.ForeignKey(default=None, to='lxca.MyOrder'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='architectapplication',
            name='compatible_servers',
            field=models.ManyToManyField(to='lxca.CatalogServer'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='architectfirmwarerepo',
            name='firmware_pack',
            field=models.FilePathField(recursive=True, blank=True, path=b'/home/lenovo', null=True, match=b'pack[.]zip'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='architectfirmwarerepo',
            name='update_access_location',
            field=models.FilePathField(recursive=True, blank=True, path=b'/home/lenovo', null=True, match=b'foo.*'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='architectrack',
            name='rack',
            field=models.ForeignKey(to='lxca.CatalogRack'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Rack',
        ),
        migrations.AlterField(
            model_name='architectserver',
            name='server',
            field=models.ForeignKey(to='lxca.CatalogServer'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Server',
        ),
        migrations.AlterField(
            model_name='architectsolution',
            name='parent',
            field=models.ForeignKey(default=None, blank=True, to='lxca.ArchitectSolution', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='architectswitch',
            name='switch',
            field=models.ForeignKey(to='lxca.CatalogSwitch'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Switch',
        ),
    ]
