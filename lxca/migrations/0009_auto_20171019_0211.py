# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0008_auto_20171019_0121'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchitectConfigPattern',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('filename', models.CharField(default=b'configpatter.tgz', max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='architectbasemodel',
            name='config_pattern',
            field=models.ForeignKey(default=1, to='lxca.ArchitectConfigPattern'),
            preserve_default=False,
        ),
    ]
