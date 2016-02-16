# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0030_mysalesorder_default_storage'),
    ]

    operations = [
        migrations.CreateModel(
            name='MySizeChart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('size', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='myitem',
            name='size_chart',
            field=models.ForeignKey(default=1, to='erp.MySizeChart'),
            preserve_default=False,
        ),
    ]
