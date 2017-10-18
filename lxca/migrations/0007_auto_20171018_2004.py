# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0006_auto_20171018_1938'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchitectCompliance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'compliance', max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='architectsolution',
            name='compliance',
            field=models.ForeignKey(default=1, to='lxca.ArchitectCompliance'),
            preserve_default=False,
        ),
    ]
