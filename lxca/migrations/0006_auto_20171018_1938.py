# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0005_remove_architectsolution_firmware_repo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchitectLxca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.CharField(max_length=8)),
                ('patch_update_filename', models.CharField(default=b'update.tgz', max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='architectsolution',
            name='lxca',
            field=models.ForeignKey(default=1, to='lxca.ArchitectLxca'),
            preserve_default=False,
        ),
    ]
