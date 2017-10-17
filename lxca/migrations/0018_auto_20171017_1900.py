# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0017_auto_20171017_1842'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchitectPdu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('catalog', models.ForeignKey(to='lxca.CatalogPdu')),
                ('rule_for_count', models.ForeignKey(to='lxca.ArchitectRuleForCount')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='architectsolution',
            name='powers',
            field=models.ManyToManyField(to='lxca.ArchitectPdu'),
            preserve_default=True,
        ),
    ]
