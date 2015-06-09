# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0004_myapplication_application_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyApplicationStatusHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=16, verbose_name='Status')),
                ('contact', models.CharField(max_length=128, verbose_name='Contact person')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('application', models.ForeignKey(verbose_name='Application', to='intern.MyApplication')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
