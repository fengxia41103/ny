# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0018_auto_20171020_1957'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyCharm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('host', models.IntegerField(default=2, choices=[(1, 'Ubuntu 16.04 Xeniel'), (2, 'Ubuntu 14.04 Trusty'), (3, 'Cent 7.0'), (4, 'RHEL 7.4')])),
                ('name', models.CharField(max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='architectendpoint',
            name='charm',
            field=models.ForeignKey(blank=True, to='lxca.MyCharm', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='architectsolution',
            name='charm',
            field=models.ForeignKey(blank=True, to='lxca.MyCharm', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='orderserver',
            name='layer0',
            field=models.IntegerField(default=6, choices=[(1, 'Windows Server 2010'), (2, 'ESXI server'), (3, 'Ubuntu 16.04 Xeniel'), (4, 'Ubuntu 14.04 Trusty'), (5, 'Cent 7.0'), (6, 'RHEL 7.4')]),
            preserve_default=True,
        ),
    ]
