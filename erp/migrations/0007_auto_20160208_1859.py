# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0006_auto_20160208_1848'),
    ]

    operations = [
        migrations.CreateModel(
            name='MySeason',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=8)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='myglaccount',
            name='gl_group',
        ),
        migrations.RemoveField(
            model_name='myglgroup',
            name='gl_class',
        ),
        migrations.DeleteModel(
            name='MyGLClass',
        ),
        migrations.RemoveField(
            model_name='myglgroup',
            name='subgroup_of',
        ),
        migrations.DeleteModel(
            name='MyGLGroup',
        ),
        migrations.RemoveField(
            model_name='myitemcategory',
            name='adjustment_gl',
        ),
        migrations.RemoveField(
            model_name='myitemcategory',
            name='cogs_gl',
        ),
        migrations.RemoveField(
            model_name='myitemcategory',
            name='inventory_gl',
        ),
        migrations.RemoveField(
            model_name='myitemcategory',
            name='sales_gl',
        ),
        migrations.DeleteModel(
            name='MyGLAccount',
        ),
        migrations.RemoveField(
            model_name='myitemcategory',
            name='uom',
        ),
        migrations.RemoveField(
            model_name='myitem',
            name='category',
        ),
        migrations.DeleteModel(
            name='MyItemCategory',
        ),
        migrations.RemoveField(
            model_name='myvendoritem',
            name='discount',
        ),
        migrations.AddField(
            model_name='myitem',
            name='currency',
            field=models.ForeignKey(default=None, to='erp.MyCurrency'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myitem',
            name='price',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myitem',
            name='season',
            field=models.ForeignKey(default=None, to='erp.MySeason'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myvendor',
            name='price_discount',
            field=models.FloatField(default=0.25),
            preserve_default=True,
        ),
    ]
