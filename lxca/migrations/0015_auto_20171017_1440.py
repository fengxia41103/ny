# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lxca', '0014_auto_20171017_1428'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='pduinput',
            unique_together=set([('voltage', 'phase', 'current')]),
        ),
        migrations.AlterUniqueTogether(
            name='pduoutput',
            unique_together=set([('voltage', 'capacity', 'power_limit_per_pdu', 'power_limit_per_outlet', 'power_limit_per_group')]),
        ),
    ]
