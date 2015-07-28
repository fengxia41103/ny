# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0013_auto_20150616_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyBox',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('size', models.CharField(max_length=1, verbose_name='Box size', choices=[(b'L', b'LCHOICEarge'), (b'M', b'Medium'), (b'S', b'Small')])),
                ('weight', models.FloatField(default=0.0, verbose_name='Actual weight')),
                ('status', models.CharField(max_length=8, verbose_name='Status', choices=[(b'E', b'Empty'), (b'I', b'In packing'), (b'S', b'Sealed'), (b'R', b'Shipped, in route'), (b'D', b'Delivered'), (b'U', b'Unpacking'), (b'G', b'In strorage'), (b'B', b'Broken'), (b'M', b'Missing')])),
                ('valuable_index', models.IntegerField(default=0, verbose_name='How valuable to me', choices=[(1, b'Unimportant'), (2, b'Some important'), (3, b'Important'), (4, b'Very important'), (5, b'Must have')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MyItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hash', models.CharField(default=b'', max_length=256, null=True, verbose_name='MD5 hash', blank=True)),
                ('name', models.CharField(default=None, max_length=128, verbose_name='\u540d\u79f0')),
                ('description', models.TextField(null=True, verbose_name='\u63cf\u8ff0', blank=True)),
                ('help_text', models.CharField(max_length=64, null=True, verbose_name='\u5e2e\u52a9\u63d0\u793a', blank=True)),
                ('fate', models.CharField(max_length=1, verbose_name='End result for this item', choices=[(b'P', b'Pending'), (b'G', b'Goodwill'), (b'B', b'Boxed'), (b'D', b'Disposed')])),
                ('box', models.ManyToManyField(to='intern.MyBox', verbose_name='In box')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MyRoom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name='Room name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='myitem',
            name='home_room',
            field=models.ManyToManyField(to='intern.MyRoom', verbose_name='Home room'),
            preserve_default=True,
        ),
    ]
