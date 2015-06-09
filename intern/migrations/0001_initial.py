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
            name='Attachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
                ('name', models.CharField(default=b'default name', max_length=64, verbose_name='\u9644\u4ef6\u540d\u79f0')),
                ('description', models.CharField(default=b'default description', max_length=64, verbose_name='\u9644\u4ef6\u63cf\u8ff0')),
                ('file', models.FileField(help_text='\u9644\u4ef6', upload_to=b'%Y/%m/%d', verbose_name='\u9644\u4ef6')),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('created_by', models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL, blank=True, help_text=b'', null=True, verbose_name='\u521b\u5efa\u7528\u6237')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MyApplication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hash', models.CharField(default=b'', max_length=256, null=True, verbose_name='MD5 hash', blank=True)),
                ('name', models.CharField(default=None, max_length=128, verbose_name='\u540d\u79f0')),
                ('description', models.TextField(null=True, verbose_name='\u63cf\u8ff0', blank=True)),
                ('help_text', models.CharField(max_length=64, null=True, verbose_name='\u5e2e\u52a9\u63d0\u793a', blank=True)),
                ('applicant_name', models.CharField(max_length=256, verbose_name='Applicant name')),
                ('start_date', models.DateField(verbose_name='Starting date')),
                ('end_date', models.DateField(verbose_name='End date')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MyApplicationComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('summary', models.CharField(max_length=512, verbose_name='Comment summary')),
                ('detail', models.TextField(null=True, verbose_name='Comment details', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MyExternalContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hash', models.CharField(default=b'', max_length=256, null=True, verbose_name='MD5 hash', blank=True)),
                ('name', models.CharField(default=None, max_length=128, verbose_name='\u540d\u79f0')),
                ('description', models.TextField(null=True, verbose_name='\u63cf\u8ff0', blank=True)),
                ('help_text', models.CharField(max_length=64, null=True, verbose_name='\u5e2e\u52a9\u63d0\u793a', blank=True)),
                ('email', models.EmailField(max_length=75)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MyStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=1, choices=[(1, 'initialized'), (2, 'dept submitted'), (3, 'college submitted'), (4, 'approved')])),
                ('contact', models.ForeignKey(verbose_name='Conact in charge', to='intern.MyExternalContact')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MyTaggedItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.SlugField(default=b'', max_length=16, verbose_name='Tag')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='myapplication',
            name='comments',
            field=models.ManyToManyField(related_name='applications', verbose_name='Comments', to='intern.MyApplicationComment'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myapplication',
            name='status',
            field=models.ForeignKey(verbose_name='Application status', to='intern.MyStatus'),
            preserve_default=True,
        ),
    ]
