# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0019_auto_20150727_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='mybox',
            name='unpack_priority',
            field=models.IntegerField(default=1, verbose_name='Priority to unpack', choices=[(1, b'Can live without'), (2, b'Nice to have'), (3, b'Need but can wait'), (4, b'Need now'), (5, b'Die if missing')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mybox',
            name='valuable_index',
            field=models.IntegerField(default=1, verbose_name='How valuable to me', choices=[(1, b'Unimportant'), (2, b'Some important'), (3, b'Important'), (4, b'Very important'), (5, b'Must have')]),
            preserve_default=True,
        ),
    ]
