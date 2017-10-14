# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import annoying.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playbook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('path', models.FilePathField()),
                ('tags', models.CharField(default=b'', max_length=32)),
                ('extra_vars', annoying.fields.JSONField(default=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='storagedisk',
            old_name='capacity_in_gb',
            new_name='capacity',
        ),
    ]
