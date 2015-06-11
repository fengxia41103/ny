# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0009_myapplication_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='MySponsor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name='Sponsor name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='myapplication',
            name='affiliated_id',
            field=models.CharField(max_length=64, null=True, verbose_name='Affiliated ID', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myapplication',
            name='sponsor',
            field=models.ForeignKey(verbose_name='Sponsor', blank=True, to='intern.MySponsor', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mystatus',
            name='status',
            field=models.IntegerField(default=1, choices=[(1, 'initialized'), (2, 'dept approval'), (3, 'college approval'), (4, 'route to C&G'), (5, 'contract draft send to sponsor'), (6, 'contract negotiation'), (7, 'contract terms finalized'), (8, 'students signs off'), (9, 'C&G signs off'), (10, 'sponsor signs off - fully executed'), (11, 'college post-award update')]),
            preserve_default=True,
        ),
    ]
