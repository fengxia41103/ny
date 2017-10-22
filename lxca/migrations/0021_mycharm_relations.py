# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0020_architectsolution_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycharm',
            name='relations',
            field=models.ManyToManyField(related_name='relations_rel_+', to='lxca.MyCharm', blank=True),
            preserve_default=True,
        ),
    ]
