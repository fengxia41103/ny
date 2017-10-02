# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0004_auto_20170920_1840'),
    ]

    operations = [
        migrations.CreateModel(
            name='FirmwareRepo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('update_access_method', models.CharField(default=b'm', max_length=8, choices=[(b'm', b'manual')])),
                ('update_access_location', models.FilePathField(path=b'/home/lenovo', recursive=True, match=b'foo.*')),
                ('pack', models.FilePathField(path=b'/home/lenovo', recursive=True, match=b'pack[.]zip')),
                ('fix', models.CharField(default=b'fixid', max_length=8)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FirmwareRepoPolicy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'repo policy', max_length=32)),
                ('device', models.CharField(default=b'policity device', max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='solution',
            name='internal_major_version',
        ),
        migrations.RemoveField(
            model_name='solution',
            name='internal_minor_version',
        ),
        migrations.RemoveField(
            model_name='solution',
            name='internal_name',
        ),
        migrations.AddField(
            model_name='solution',
            name='manifestversion_major',
            field=models.CharField(default=b'0', max_length=8),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='solution',
            name='manifestversion_minor',
            field=models.CharField(default=b'1', max_length=8),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='switch',
            name='rear_to_front',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
