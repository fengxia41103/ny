# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0013_auto_20171017_1241'),
    ]

    operations = [
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
                ('power_limit_per_group', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='catalogpdu',
            name='voltage',
        ),
        migrations.AddField(
            model_name='catalogpdu',
            name='c13',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='catalogpdu',
            name='c19',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='catalogpdu',
            name='inputs',
            field=models.ManyToManyField(to='lxca.PduInput'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='catalogpdu',
            name='is_monitored',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='catalogpdu',
            name='outputs',
            field=models.ManyToManyField(to='lxca.PduOutput'),
            preserve_default=True,
        ),
    ]
