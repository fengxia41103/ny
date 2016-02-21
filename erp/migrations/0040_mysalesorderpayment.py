# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('erp', '0039_auto_20160220_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='MySalesOrderPayment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('reviewed_on', models.DateField(default=None, null=True, blank=True)),
                ('last_modified_on', models.DateField(auto_now=True)),
                ('amount', models.FloatField(default=0)),
                ('payment_method', models.CharField(default=b'Cash', max_length=16, choices=[(b'Cash', b'Cash'), (b'Paypal', b'Paypal'), ('\u652f\u4ed8\u5b9d', '\u652f\u4ed8\u5b9d'), ('\u5fae\u4fe1\u652f\u4ed8', '\u5fae\u4fe1\u652f\u4ed8')])),
                ('created_by', models.ForeignKey(related_name='Logger', verbose_name='\u521b\u5efa\u7528\u6237', to=settings.AUTH_USER_MODEL, help_text=b'')),
                ('reviewed_by', models.ForeignKey(related_name='Reviewer', default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('so', models.ForeignKey(to='erp.MySalesOrder')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
