# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


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
                ('name', models.CharField(max_length=32)),
                ('host', models.CharField(max_length=32, choices=[(b'bm', b'BareMetal'), (b'win210svr', b'Windows Server 2010'), (b'esxi', b'ESXI server'), (b'Ubuntu xeniel', b'Ubuntu 16.04 Xeniel'), (b'Ubuntu trusty', b'Ubuntu 14.04 Trusty')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArchitectFirmwareRepo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('update_access_method', models.CharField(default=b'm', max_length=8, choices=[(b'm', b'manual')])),
                ('update_access_location', models.FilePathField(path=b'/home/lenovo', recursive=True, match=b'foo.*')),
                ('firmware_pack', models.FilePathField(path=b'/home/lenovo', recursive=True, match=b'pack[.]zip')),
                ('firmware_fix_id', models.CharField(default=b'fixid', max_length=8)),
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
            name='ArchitectRack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rule_for_count', models.ForeignKey(to='lxca.ArchitectRuleForCount')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArchitectSolution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='default name', max_length=128)),
                ('description', models.TextField(default=b'')),
                ('help_text', models.CharField(max_length=64, null=True, verbose_name='Help', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('manifestversion_major', models.CharField(default=b'0', max_length=8)),
                ('manifestversion_minor', models.CharField(default=b'1', max_length=8)),
                ('applications', models.ManyToManyField(to='lxca.ArchitectApplication')),
                ('firmware_policy', models.ForeignKey(to='lxca.ArchitectFirmwareRepoPolicy')),
                ('firmware_repo', models.ForeignKey(to='lxca.ArchitectFirmwareRepo')),
                ('parent', models.ForeignKey(default=None, blank=True, to='lxca.ArchitectSolution', null=True, verbose_name='Solution')),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rule_for_count', models.ForeignKey(to='lxca.ArchitectRuleForCount')),
            ],
            options={
            },
            bases=(models.Model,),
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
                ('mtm', models.CharField(default=b'mtm', max_length=64)),
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
                ('mtm', models.CharField(default=b'mtm', max_length=64)),
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
                ('mtm', models.CharField(default=b'mtm', max_length=64)),
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
                ('count', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderRack',
            fields=[
                ('orderbasemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='lxca.OrderBaseModel')),
                ('rack', models.ForeignKey(to='lxca.ArchitectRack')),
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
                ('ip', models.GenericIPAddressField()),
                ('server', models.ForeignKey(to='lxca.ArchitectServer')),
            ],
            options={
            },
            bases=('lxca.orderbasemodel',),
        ),
        migrations.CreateModel(
            name='OrderSolution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('racks', models.ManyToManyField(to='lxca.OrderRack')),
                ('servers', models.ManyToManyField(to='lxca.OrderServer')),
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
                ('switch', models.ForeignKey(to='lxca.ArchitectSwitch')),
            ],
            options={
            },
            bases=('lxca.orderbasemodel',),
        ),
        migrations.CreateModel(
            name='PDU',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='default name', max_length=128)),
                ('description', models.TextField(default=b'')),
                ('help_text', models.CharField(max_length=64, null=True, verbose_name='Help', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('size', models.CharField(default='1U', max_length=8, choices=[('1U', '1U'), ('2U', '2U')])),
                ('voltage', models.CharField(default='120-1', max_length=16, choices=[('120-1', '120V single phase'), ('208-1', '208V single phase'), ('120-3', '208V three phase'), ('400-3', '400V three phase')])),
                ('orientation', models.CharField(default='h', max_length=16, choices=[('h', 'Horizontal'), ('v', 'Vertical')])),
                ('form_factor', models.IntegerField(default=1, help_text='0=vertical mount, 1=1U, 2=2U, and so on', verbose_name='Form factor')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='default name', max_length=128)),
                ('description', models.TextField(default=b'')),
                ('help_text', models.CharField(max_length=64, null=True, verbose_name='Help', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_primary', models.BooleanField(default=True, verbose_name='Is primary rack')),
                ('size', models.CharField(default='16U', max_length=8, choices=[('16U', '16U'), ('32U', '32U'), ('48U', '48U')])),
                ('width', models.FloatField(default=19, verbose_name=b'Rack width (inch)')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RaidAdapter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='default name', max_length=128)),
                ('description', models.TextField(default=b'')),
                ('help_text', models.CharField(max_length=64, null=True, verbose_name='Help', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('size', models.CharField(default='1U', max_length=8, choices=[('1U', '1U'), ('2U', '2U')])),
                ('speed', models.CharField(default='PCIx1', max_length=32, verbose_name='PCI speed', choices=[(b'PCIx1', b'PCIx1'), (b'PCIx4', b'PCIx4'), (b'PCIx6', b'PCIx6')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='default name', max_length=128)),
                ('description', models.TextField(default=b'')),
                ('help_text', models.CharField(max_length=64, null=True, verbose_name='Help', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('size', models.CharField(default='1U', max_length=8, choices=[('1U', '1U'), ('2U', '2U')])),
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
        migrations.CreateModel(
            name='Switch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='default name', max_length=128)),
                ('description', models.TextField(default=b'')),
                ('help_text', models.CharField(max_length=64, null=True, verbose_name='Help', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('size', models.CharField(default='1U', max_length=8, choices=[('1U', '1U'), ('2U', '2U')])),
                ('speed', models.CharField(default='1G', max_length=8, choices=[('1G', '1G'), ('10G', '10G')])),
                ('cooling_orientation', models.CharField(default='h', max_length=8, verbose_name='Cooling orientation', choices=[('h', 'Horizontal'), ('v', 'Vertical')])),
                ('rear_to_front', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
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
        migrations.AddField(
            model_name='ordersolution',
            name='switches',
            field=models.ManyToManyField(to='lxca.OrderSwitch'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orderserver',
            name='storages',
            field=models.ManyToManyField(to='lxca.StorageDisk'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mfgswitch',
            name='switch',
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
            name='server',
            field=models.ForeignKey(to='lxca.OrderServer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mfgrack',
            name='rack',
            field=models.ForeignKey(to='lxca.OrderRack'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='architectswitch',
            name='switch',
            field=models.ForeignKey(to='lxca.Switch'),
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
            name='server',
            field=models.ForeignKey(to='lxca.Server'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='architectrack',
            name='rack',
            field=models.ForeignKey(to='lxca.Rack'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='architectrack',
            name='rule_for_count',
            field=models.ForeignKey(to='lxca.ArchitectRuleForCount'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='architectapplication',
            name='compatible_servers',
            field=models.ManyToManyField(to='lxca.Server'),
            preserve_default=True,
        ),
    ]
