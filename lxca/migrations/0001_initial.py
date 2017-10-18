# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import annoying.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchitectApplication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='default name', max_length=128)),
                ('description', models.TextField(default=b'')),
                ('is_active', models.BooleanField(default=True)),
                ('host', models.CharField(max_length=32, choices=[(b'bm', b'BareMetal'), (b'win210svr', b'Windows Server 2010'), (b'esxi', b'ESXI server'), (b'Ubuntu xeniel', b'Ubuntu 16.04 Xeniel'), (b'Ubuntu trusty', b'Ubuntu 14.04 Trusty')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArchitectBaseModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArchitectFirmwareRepo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firmware_fix_id', models.CharField(default=b'fixid', max_length=8)),
                ('update_access_method', models.CharField(default=b'm', max_length=8, choices=[(b'm', b'manual')])),
                ('update_access_location', models.FilePathField(recursive=True, blank=True, path=b'/home/lenovo', null=True, match=b'foo.*')),
                ('firmware_pack', models.FilePathField(recursive=True, blank=True, path=b'/home/lenovo', null=True, match=b'pack[.]zip')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArchitectFirmwareRepoPolicy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'repo policy', max_length=32)),
                ('device', models.CharField(default=b'policity device', max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArchitectPdu',
            fields=[
                ('architectbasemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='lxca.ArchitectBaseModel')),
            ],
            options={
            },
            bases=('lxca.architectbasemodel',),
        ),
        migrations.CreateModel(
            name='ArchitectRack',
            fields=[
                ('architectbasemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='lxca.ArchitectBaseModel')),
            ],
            options={
            },
            bases=('lxca.architectbasemodel',),
        ),
        migrations.CreateModel(
            name='ArchitectRuleForCount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('max_count', models.IntegerField(default=0)),
                ('min_count', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArchitectServer',
            fields=[
                ('architectbasemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='lxca.ArchitectBaseModel')),
            ],
            options={
            },
            bases=('lxca.architectbasemodel',),
        ),
        migrations.CreateModel(
            name='ArchitectSolution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='default name', max_length=128)),
                ('description', models.TextField(default=b'')),
                ('is_active', models.BooleanField(default=True)),
                ('version', models.CharField(max_length=8)),
                ('applications', models.ManyToManyField(to='lxca.ArchitectApplication')),
                ('firmware_policy', models.ForeignKey(to='lxca.ArchitectFirmwareRepoPolicy')),
                ('firmware_repo', models.ForeignKey(to='lxca.ArchitectFirmwareRepo')),
                ('parent', models.ForeignKey(default=None, blank=True, to='lxca.ArchitectSolution', null=True)),
                ('powers', models.ManyToManyField(to='lxca.ArchitectPdu')),
                ('racks', models.ManyToManyField(to='lxca.ArchitectRack')),
                ('servers', models.ManyToManyField(to='lxca.ArchitectServer')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArchitectSwitch',
            fields=[
                ('architectbasemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='lxca.ArchitectBaseModel')),
            ],
            options={
            },
            bases=('lxca.architectbasemodel',),
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
                ('name', models.CharField(default=b'default name', max_length=64)),
                ('description', models.CharField(default=b'default description', max_length=64)),
                ('file', models.FileField(upload_to=b'%Y/%m/%d', verbose_name='Attachment')),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('created_by', models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL, blank=True, help_text=b'', null=True, verbose_name='Creator')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CatalogPdu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='default name', max_length=128)),
                ('description', models.TextField(default=b'')),
                ('is_active', models.BooleanField(default=True)),
                ('size', models.IntegerField(default=1, choices=[(0, '0U'), (1, '1U'), (2, '2U')])),
                ('orientation', models.CharField(default='h', max_length=16, choices=[('h', 'Horizontal'), ('v', 'Vertical')])),
                ('c13', models.IntegerField(default=0)),
                ('c19', models.IntegerField(default=0)),
                ('is_monitored', models.BooleanField(default=False)),
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
                ('is_active', models.BooleanField(default=True)),
                ('is_primary', models.BooleanField(default=True, verbose_name='Is primary rack')),
                ('eia_capacity', models.IntegerField(default=25, choices=[(25, '25U'), (42, '42U')])),
                ('sidewall_compartment', models.IntegerField(default=0)),
                ('expansion_rack', models.ForeignKey(default=None, blank=True, to='lxca.CatalogRack', help_text=b'Expansion rack for the primary', null=True)),
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
                ('is_active', models.BooleanField(default=True)),
                ('size', models.IntegerField(default=1, choices=[(0, '0U'), (1, '1U'), (2, '2U')])),
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
                ('is_active', models.BooleanField(default=True)),
                ('size', models.IntegerField(default=1, choices=[(0, '0U'), (1, '1U'), (2, '2U')])),
                ('orientation', models.CharField(default='h', max_length=16, choices=[('h', 'Horizontal'), ('v', 'Vertical')])),
                ('cpu_sockets', models.IntegerField(default=2)),
                ('max_25_disk', models.IntegerField(default=12, help_text='Maximum number of 2.5inch disks')),
                ('max_35_disk', models.IntegerField(default=10)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CatalogStorageDisk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('physical_format', models.CharField(default=b'2.5', max_length=8, choices=[(b'2.5', b'2.5 inch'), (b'3.5', b'3.5 inch'), (b'ssd', b'ssd')])),
                ('capacity', models.IntegerField(default=100, help_text='Storage capacity in GB.')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CatalogSwitch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='default name', max_length=128)),
                ('description', models.TextField(default=b'')),
                ('is_active', models.BooleanField(default=True)),
                ('size', models.IntegerField(default=1, choices=[(0, '0U'), (1, '1U'), (2, '2U')])),
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
            name='MfgRack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bm_user', models.CharField(default=b'', max_length=64)),
                ('bm_password', models.CharField(default=b'', max_length=32)),
                ('bm_manager_url', models.URLField(default=b'')),
                ('imm_ip', models.GenericIPAddressField(null=True, blank=True)),
                ('imm_user', models.CharField(default=b'', max_length=64)),
                ('imm_password', models.CharField(default=b'', max_length=32)),
                ('serial', models.CharField(max_length=64, null=True, verbose_name='Serial number', blank=True)),
                ('uuid', models.CharField(default=b'uuid', max_length=32)),
                ('mtm', models.CharField(default=b'', help_text=b'Machine type model', max_length=64)),
                ('firmware_update', models.CharField(default=b'', max_length=32)),
                ('config_pattern', models.CharField(default=b'', max_length=32)),
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
                ('bm_user', models.CharField(default=b'', max_length=64)),
                ('bm_password', models.CharField(default=b'', max_length=32)),
                ('bm_manager_url', models.URLField(default=b'')),
                ('imm_ip', models.GenericIPAddressField(null=True, blank=True)),
                ('imm_user', models.CharField(default=b'', max_length=64)),
                ('imm_password', models.CharField(default=b'', max_length=32)),
                ('serial', models.CharField(max_length=64, null=True, verbose_name='Serial number', blank=True)),
                ('uuid', models.CharField(default=b'uuid', max_length=32)),
                ('mtm', models.CharField(default=b'', help_text=b'Machine type model', max_length=64)),
                ('firmware_update', models.CharField(default=b'', max_length=32)),
                ('config_pattern', models.CharField(default=b'', max_length=32)),
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
                ('racks', models.ManyToManyField(to='lxca.MfgRack')),
                ('servers', models.ManyToManyField(to='lxca.MfgServer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MfgSwitch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bm_user', models.CharField(default=b'', max_length=64)),
                ('bm_password', models.CharField(default=b'', max_length=32)),
                ('bm_manager_url', models.URLField(default=b'')),
                ('imm_ip', models.GenericIPAddressField(null=True, blank=True)),
                ('imm_user', models.CharField(default=b'', max_length=64)),
                ('imm_password', models.CharField(default=b'', max_length=32)),
                ('serial', models.CharField(max_length=64, null=True, verbose_name='Serial number', blank=True)),
                ('uuid', models.CharField(default=b'uuid', max_length=32)),
                ('mtm', models.CharField(default=b'', help_text=b'Machine type model', max_length=64)),
                ('firmware_update', models.CharField(default=b'', max_length=32)),
                ('config_pattern', models.CharField(default=b'', max_length=32)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content', models.TextField(verbose_name='Note')),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderBaseModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qty', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderApplication',
            fields=[
                ('orderbasemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='lxca.OrderBaseModel')),
                ('template', models.ForeignKey(to='lxca.ArchitectApplication')),
            ],
            options={
            },
            bases=('lxca.orderbasemodel',),
        ),
        migrations.CreateModel(
            name='OrderPdu',
            fields=[
                ('orderbasemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='lxca.OrderBaseModel')),
                ('template', models.ForeignKey(to='lxca.ArchitectPdu')),
            ],
            options={
            },
            bases=('lxca.orderbasemodel',),
        ),
        migrations.CreateModel(
            name='OrderRack',
            fields=[
                ('orderbasemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='lxca.OrderBaseModel')),
                ('template', models.ForeignKey(to='lxca.ArchitectRack')),
            ],
            options={
            },
            bases=('lxca.orderbasemodel',),
        ),
        migrations.CreateModel(
            name='OrderServer',
            fields=[
                ('orderbasemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='lxca.OrderBaseModel')),
                ('firmware', models.CharField(default=b'firmware version', max_length=32)),
                ('cores', models.IntegerField(default=2)),
                ('mem', models.IntegerField(default=16, help_text='Memory size in GB')),
                ('ip', models.GenericIPAddressField(null=True, verbose_name='IP4 address', blank=True)),
                ('storages', models.ManyToManyField(to='lxca.CatalogStorageDisk')),
                ('template', models.ForeignKey(to='lxca.ArchitectServer')),
            ],
            options={
            },
            bases=('lxca.orderbasemodel',),
        ),
        migrations.CreateModel(
            name='OrderSolution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.CharField(default=b'21873', help_text='Order number', unique=True, max_length=32)),
                ('status', models.IntegerField(default=1, choices=[(1, 'draft'), (2, 'in MFG'), (3, 'in provisioning'), (4, 'in deployment'), (5, 'obsolete')])),
                ('solution', models.ForeignKey(to='lxca.ArchitectSolution')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderSwitch',
            fields=[
                ('orderbasemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='lxca.OrderBaseModel')),
                ('template', models.ForeignKey(to='lxca.ArchitectSwitch')),
            ],
            options={
            },
            bases=('lxca.orderbasemodel',),
        ),
        migrations.CreateModel(
            name='PduInput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('voltage', models.IntegerField(default=120)),
                ('phase', models.IntegerField(default=1, choices=[(1, '1 Phase'), (3, '3 Phase')])),
                ('frequency', models.IntegerField(default=1, choices=[(1, '50-60Hz')])),
                ('current', models.IntegerField(default=13)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PduOutput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('voltage', models.IntegerField(default=120)),
                ('capacity', models.IntegerField(help_text='Capacity per PDU (w)')),
                ('power_limit_per_pdu', models.IntegerField()),
                ('power_limit_per_outlet', models.IntegerField()),
                ('power_limit_per_group', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Playbook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('path', models.FilePathField()),
                ('tags', models.CharField(default=b'', max_length=32)),
                ('extra_vars', annoying.fields.JSONField(default=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaggedItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.SlugField(default=b'', max_length=16, verbose_name='Tag')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='pduoutput',
            unique_together=set([('voltage', 'capacity', 'power_limit_per_pdu', 'power_limit_per_outlet', 'power_limit_per_group')]),
        ),
        migrations.AlterUniqueTogether(
            name='pduinput',
            unique_together=set([('voltage', 'phase', 'current')]),
        ),
        migrations.AddField(
            model_name='orderbasemodel',
            name='order',
            field=models.ForeignKey(to='lxca.OrderSolution'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mfgswitch',
            name='on_order',
            field=models.ForeignKey(to='lxca.OrderSwitch'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mfgsolution',
            name='switches',
            field=models.ManyToManyField(to='lxca.MfgSwitch'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mfgserver',
            name='on_order',
            field=models.ForeignKey(to='lxca.OrderServer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mfgrack',
            name='on_order',
            field=models.ForeignKey(to='lxca.OrderRack'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='catalogpdu',
            name='inputs',
            field=models.ManyToManyField(to='lxca.PduInput'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='catalogpdu',
            name='outputs',
            field=models.ManyToManyField(to='lxca.PduOutput'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='architectswitch',
            name='catalog',
            field=models.ForeignKey(to='lxca.CatalogSwitch'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='architectsolution',
            name='switches',
            field=models.ManyToManyField(to='lxca.ArchitectSwitch'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='architectserver',
            name='catalog',
            field=models.ForeignKey(to='lxca.CatalogServer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='architectrack',
            name='catalog',
            field=models.ForeignKey(to='lxca.CatalogRack'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='architectpdu',
            name='catalog',
            field=models.ForeignKey(to='lxca.CatalogPdu'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='architectbasemodel',
            name='rule_for_count',
            field=models.ForeignKey(to='lxca.ArchitectRuleForCount'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='architectapplication',
            name='compatible_servers',
            field=models.ManyToManyField(to='lxca.CatalogServer'),
            preserve_default=True,
        ),
    ]
