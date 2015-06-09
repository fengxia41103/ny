# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0005_myapplicationstatushistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyStatusAudit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=16, verbose_name='Status')),
                ('contact', models.CharField(max_length=128, verbose_name='Contact person')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField(null=True, verbose_name='Status change comment', blank=True)),
                ('application', models.ForeignKey(verbose_name='Application', to='intern.MyApplication')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='myapplicationstatushistory',
            name='application',
        ),
        migrations.DeleteModel(
            name='MyApplicationStatusHistory',
        ),
        migrations.RemoveField(
            model_name='myapplication',
            name='comments',
        ),
        migrations.DeleteModel(
            name='MyApplicationComment',
        ),
    ]
