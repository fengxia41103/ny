# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0002_auto_20171018_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchitectFirmwarePolicy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'repo policy', max_length=32)),
                ('repo', models.ForeignKey(to='lxca.ArchitectFirmwareRepo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='architectsolution',
            name='firmware_policy',
        ),
        migrations.DeleteModel(
            name='ArchitectFirmwareRepoPolicy',
        ),
        migrations.AddField(
            model_name='architectbasemodel',
            name='firmware_policy',
            field=models.ForeignKey(blank=True, to='lxca.ArchitectFirmwarePolicy', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='architectfirmwarerepo',
            name='fix_id',
            field=models.CharField(default=b'fixpack', max_length=8),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='architectfirmwarerepo',
            name='pack_filename',
            field=models.CharField(default=b'fixpack.tgz', max_length=32),
            preserve_default=True,
        ),
    ]
