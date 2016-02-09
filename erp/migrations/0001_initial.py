# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
                ('name', models.CharField(default=b'default name', max_length=64, verbose_name='\u9644\u4ef6\u540d\u79f0')),
                ('description', models.CharField(default=b'default description', max_length=64, verbose_name='\u9644\u4ef6\u63cf\u8ff0')),
                ('file', models.FileField(help_text='\u9644\u4ef6', upload_to=b'%Y/%m/%d', verbose_name='\u9644\u4ef6')),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('created_by', models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL, blank=True, help_text=b'', null=True, verbose_name='\u521b\u5efa\u7528\u6237')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MyCompany',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hash', models.CharField(default=b'', max_length=256, null=True, verbose_name='MD5 hash', blank=True)),
                ('name', models.CharField(default=None, max_length=128, verbose_name='\u540d\u79f0')),
                ('description', models.TextField(null=True, verbose_name='\u63cf\u8ff0', blank=True)),
                ('abbrev', models.CharField(max_length=8, null=True, verbose_name='Abbreviation', blank=True)),
                ('help_text', models.CharField(max_length=64, null=True, verbose_name='\u5e2e\u52a9\u63d0\u793a', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('phone', models.CharField(max_length=16, null=True, verbose_name='Company phone', blank=True)),
                ('price_over_std_cost', models.FloatField(default=0.3, verbose_name='Price over STD cost')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MyCountry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, verbose_name='Country name')),
                ('abbrev', models.CharField(max_length=16, verbose_name='Country abbrev')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MyCurrency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=8, verbose_name='Currency name')),
                ('abbreviation', models.CharField(max_length=8, verbose_name='Currency abbrev')),
                ('symbol', models.CharField(max_length=8, verbose_name='Currency symbol')),
                ('hundredths', models.CharField(max_length=16, verbose_name='Hundredths')),
                ('country', models.ForeignKey(to='erp.MyCountry')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MyExchangeRate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rate', models.FloatField(default=1.0, verbose_name='Exchange rate')),
                ('foreign', models.ForeignKey(related_name='foreign_currency', to='erp.MyCurrency')),
                ('home', models.ForeignKey(related_name='home_currency', to='erp.MyCurrency')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MyFiscalYear',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('begin', models.DateField(verbose_name='Fiscial year start')),
                ('end', models.DateField(verbose_name='Fiscal year end')),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MyGLAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code_1', models.CharField(max_length=8, verbose_name='Account code 1')),
                ('code_2', models.CharField(max_length=8, null=True, verbose_name='Account code 2', blank=True)),
                ('name', models.CharField(max_length=32)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MyGLClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=16)),
                ('class_type', models.CharField(max_length=16, choices=[(b'Assets', b'Assets'), (b'Liabilities', b'Liabilities'), (b'Equity', b'Equity'), (b'Income', b'Income'), (b'COGS', b'Cost of Goods Sold'), (b'Expanse', b'Expanse')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MyGLGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gl_class', models.ForeignKey(to='erp.MyGLClass')),
                ('subgroup_of', models.ForeignKey(blank=True, to='erp.MyGLGroup', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MyItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hash', models.CharField(default=b'', max_length=256, null=True, verbose_name='MD5 hash', blank=True)),
                ('name', models.CharField(default=None, max_length=128, verbose_name='\u540d\u79f0')),
                ('description', models.TextField(null=True, verbose_name='\u63cf\u8ff0', blank=True)),
                ('abbrev', models.CharField(max_length=8, null=True, verbose_name='Abbreviation', blank=True)),
                ('help_text', models.CharField(max_length=64, null=True, verbose_name='\u5e2e\u52a9\u63d0\u793a', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('user_defined_code', models.CharField(max_length=16, null=True, blank=True)),
                ('upc_code', models.CharField(max_length=32, null=True, verbose_name='UPC code', blank=True)),
                ('ean_code', models.CharField(max_length=32, null=True, verbose_name='EAN code', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MyItemCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hash', models.CharField(default=b'', max_length=256, null=True, verbose_name='MD5 hash', blank=True)),
                ('name', models.CharField(default=None, max_length=128, verbose_name='\u540d\u79f0')),
                ('description', models.TextField(null=True, verbose_name='\u63cf\u8ff0', blank=True)),
                ('abbrev', models.CharField(max_length=8, null=True, verbose_name='Abbreviation', blank=True)),
                ('help_text', models.CharField(max_length=64, null=True, verbose_name='\u5e2e\u52a9\u63d0\u793a', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_excluded_from_sales', models.BooleanField(default=False)),
                ('adjustment_gl', models.ForeignKey(related_name='inventory adjustment GL', to='erp.MyGLAccount')),
                ('cogs_gl', models.ForeignKey(related_name='COGS GL', to='erp.MyGLAccount')),
                ('inventory_gl', models.ForeignKey(related_name='inventory GL', to='erp.MyGLAccount')),
                ('sales_gl', models.ForeignKey(related_name='sales GL', to='erp.MyGLAccount')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MyNote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content', models.TextField(verbose_name='Note')),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MyTaggedItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.SlugField(default=b'', max_length=16, verbose_name='Tag')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MyUOM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uom', models.CharField(max_length=8, verbose_name='unit of measure')),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='myitemcategory',
            name='uom',
            field=models.ForeignKey(to='erp.MyUOM'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myitem',
            name='category',
            field=models.ForeignKey(to='erp.MyItemCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myglaccount',
            name='gl_group',
            field=models.ForeignKey(to='erp.MyGLGroup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mycompany',
            name='fiscal_year',
            field=models.ForeignKey(to='erp.MyFiscalYear'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mycompany',
            name='home_currency',
            field=models.ForeignKey(to='erp.MyCurrency'),
            preserve_default=True,
        ),
    ]
