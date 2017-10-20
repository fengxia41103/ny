# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0002_auto_20171019_1526'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaremetalManager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(default=b'', max_length=64)),
                ('password', models.CharField(default=b'', max_length=32)),
                ('url', models.URLField(default=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='mfgrack',
            name='bm_manager_url',
        ),
        migrations.RemoveField(
            model_name='mfgrack',
            name='bm_password',
        ),
        migrations.RemoveField(
            model_name='mfgrack',
            name='bm_user',
        ),
        migrations.RemoveField(
            model_name='mfgserver',
            name='bm_manager_url',
        ),
        migrations.RemoveField(
            model_name='mfgserver',
            name='bm_password',
        ),
        migrations.RemoveField(
            model_name='mfgserver',
            name='bm_user',
        ),
        migrations.RemoveField(
            model_name='mfgswitch',
            name='bm_manager_url',
        ),
        migrations.RemoveField(
            model_name='mfgswitch',
            name='bm_password',
        ),
        migrations.RemoveField(
            model_name='mfgswitch',
            name='bm_user',
        ),
        migrations.AddField(
            model_name='mfgrack',
            name='bm_manager',
            field=models.ForeignKey(blank=True, to='lxca.BaremetalManager', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mfgserver',
            name='bm_manager',
            field=models.ForeignKey(blank=True, to='lxca.BaremetalManager', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mfgswitch',
            name='bm_manager',
            field=models.ForeignKey(blank=True, to='lxca.BaremetalManager', null=True),
            preserve_default=True,
        ),
    ]
