# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import annoying.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0007_auto_20171019_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='architectendpoint',
            name='playbooks',
            field=models.ManyToManyField(to='lxca.Playbook'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='architectsolution',
            name='playbooks',
            field=models.ManyToManyField(to='lxca.Playbook'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='playbook',
            name='extra_vars',
            field=annoying.fields.JSONField(default=b'', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='playbook',
            name='path',
            field=models.FilePathField(default=b'', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='playbook',
            name='tags',
            field=models.CharField(default=b'', max_length=32, null=True, blank=True),
            preserve_default=True,
        ),
    ]
