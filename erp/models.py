# -*- coding: utf-8 -*-

from django.db import models
from django.contrib import admin
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.generic import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from annoying.fields import JSONField # django-annoying
from django.db.models import Q
from datetime import datetime as dt
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from localflavor.us.forms import USPhoneNumberField


class MyBaseModel (models.Model):
	# fields
	hash = models.CharField (
		max_length = 256, # we don't expect using a hash more than 256-bit long!
		null = True,
		blank = True,
		default = '',
		verbose_name = u'MD5 hash'
	)
		
	# basic value fields
	name = models.CharField(
		default = None,
		max_length = 128,
		verbose_name = u'名称'
	)
	description = models.TextField (
		null=True, 
		blank=True,
		verbose_name = u'描述'
	)
	abbrev = models.CharField(
		max_length = 8,
		null = True,
		blank = True,
		verbose_name = u'Abbreviation'
	)
	
	# help text
	help_text = models.CharField (
		max_length = 64,
		null = True,
		blank = True,
		verbose_name = u'帮助提示'
	)

	# attachments
	attachments = GenericRelation('Attachment')
	notes = GenericRelation('MyNote')

	# is object active
	is_active = models.BooleanField(default = True)

	# this is an Abstract model
	class Meta:
		abstract=True

	def __unicode__(self):
		return self.name

######################################################
#
#	Tags
#
#####################################################
class MyTaggedItem (models.Model):
	# basic value fields
	tag = models.SlugField(
			default = '',
			max_length = 16,
			verbose_name = u'Tag'
	)	
	def __unicode__(self):
		return self.tag

######################################################
#
#	Attachments
#
#####################################################
class Attachment (models.Model):
	# generic foreign key to base model
	# so we can link attachment to any model defined below
	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	# instance fields
	created_by = models.ForeignKey (
		User,
		blank = True,
		null = True,
		default = None,
		verbose_name = u'创建用户',
		help_text = ''
	)
		
	# basic value fields
	name = models.CharField(
		default = 'default name',
		max_length = 64,
		verbose_name = u'附件名称'
	)
	description = models.CharField (
		max_length = 64,
		default = 'default description',
		verbose_name = u'附件描述'
	)
	file = models.FileField (
		upload_to = '%Y/%m/%d',
		verbose_name = u'附件',
		help_text = u'附件'
	)	

	def __unicode__(self):
		return self.file.name

######################################################
#
#	Notes
#
#####################################################
class MyNote(models.Model):
	# generic foreign key to base model
	# so we can link attachment to any model defined below
	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	content = models.TextField(
		verbose_name = u'Note'
	)

######################################################
#
#	App specific models
#
#####################################################
class MyCountry(models.Model):
	name = models.CharField(
		max_length = 64,
		verbose_name = u'Country name'
	)
	abbrev = models.CharField(
		max_length = 16,
		verbose_name = u'Country abbrev'
	)
	def __unicode__(self):
		return self.name

class MyCurrency(models.Model):
	name = models.CharField(
		max_length = 16,
		verbose_name = u'Currency name'
	)
	abbrev = models.CharField(
		max_length = 8,
		verbose_name = u'Currency abbrev'
	)
	symbol = models.CharField(
		max_length = 8,
		verbose_name = u'Currency symbol'
	)
	country = models.ForeignKey(
		'MyCountry'
	)
	def __unicode__(self):
		return self.symbol

class MyExchangeRate(models.Model):
	home = models.ForeignKey('MyCurrency', related_name = 'home_currency')
	foreign = models.ForeignKey('MyCurrency', related_name = 'foreign_currency')
	rate = models.FloatField(
		default = 1.0,
		verbose_name = u'Exchange rate'
	)

	def __unicode__(self):
		return u'%s = %s * %s' % (self.home,str(self.rate),self.foreign)

class MyUOM(models.Model):
	uom = models.CharField(
		max_length = 8,
		verbose_name = u'unit of measure'
	)
	description = models.TextField(
		null = True,
		blank = True,
	)

	def __unicode__(self):
		return self.uom

class MyFiscalYear(models.Model):
	begin = models.DateField(
		verbose_name = u'Fiscial year start'
	)
	end = models.DateField(
		verbose_name = u'Fiscal year end'
	)
	is_active = models.BooleanField(
		default = False,
	)

	def __unicode__(self):
		return '%s - %s'%(self.begin,self.end)

class MyCompany(MyBaseModel):
	home_currency = models.ForeignKey('MyCurrency')
	fiscal_year = models.ForeignKey('MyFiscalYear')

	phone = models.CharField(
		max_length = 16,
		null = True,
		blank = True,
		verbose_name = u'Company phone'
	)	

class MyLocation (models.Model):
	crm = models.ForeignKey('MyCRM')	
	name = models.CharField(
		default = None,
		max_length = 32,
		verbose_name = u'名称'
	)	
	def _code(self):
		return u'%s-%s' %(self.crm,self.name)
	code = property(_code)

	address = models.TextField()

	def __unicode__(self):
		return self.code

class MyStorage (models.Model):
	location = models.ForeignKey('MyLocation')
	def _code(self):
		return u'%s-%d' %(self.location,self.id)
	code = property(_code)

	def _physical(self):
		qty = [inv_item.physical for inv_item in MyItemInventory.objects.filter(storage=self)]
		return sum(qty)
	physical = property(_physical)

	def _theoretical(self):
		qty = [inv_item.theoretical for inv_item in MyItemInventory.objects.filter(storage=self)]
		return sum(qty)
	theoretical = property(_theoretical)

	def __unicode__(self):
		return self.code

class MyCRM(MyBaseModel):
	CRM_TYPE_CHOICES = (
		('B','Both'), # can only be WH internals
		('V','Vendor'), # can only  link to PO
		('C','Customer') # can only link to SO
	)
	crm_type = models.CharField(
		max_length = 16,
		default = 'vendor',
		choices = CRM_TYPE_CHOICES
	)
	contact = models.CharField(
		max_length = 32,
		null = True,
		blank = True,
		verbose_name = u'CRM contact'
	)	
	phone = models.CharField(
		max_length = 16,
		null = True,
		blank = True,
		verbose_name = u'Vendor phone'
	)
	balance = models.FloatField(default = 0)
	home_currency = models.ForeignKey('MyCurrency')
	std_discount = models.FloatField(default=0.25)
	
class MyVendorItem(models.Model):
	vendor = models.ForeignKey('MyCRM')
	sku = models.CharField(
		max_length = 32,
		default = '',
	)
	price = models.FloatField(default = 0)
	currency = models.ForeignKey('MyCurrency')
	product = models.ForeignKey('MyItem')

class MySeason(models.Model):
	name = models.CharField(
		max_length = 8
	)
	def __unicode__(self):
		return self.name

class MyItem(MyBaseModel):
	'''
	Attachment would be item photos.
	'''
	season = models.ForeignKey('MySeason')
	brand = models.ForeignKey('MyCRM', verbose_name=u'品牌')
	color = models.CharField(
		max_length = 128,
		default = '',
	)
	price = models.FloatField(default = 0)
	currency = models.ForeignKey('MyCurrency')

	# If we know when is the deadline to place SO
	# against this item. This is observed when showing items
	# available for SO on e-Commerce site.
	order_deadline = models.DateField(
		null = True,
		blank = True,
	)

	def _code(self):
		return u'%s-%s' %(self.name,self.color)
	code = property(_code)

	def _multiplier(self):
		vendor_item = MyVendorItem.objects.filter(product=self,vendor=self.brand)[0]
		exchange_rate = None
		converted_cost = 0
		try:
			exchange_rate = MyExchangeRate.objects.get(home=self.currency, foreign=vendor_item.currency)
			converted_cost = vendor_item.price / exchange_rate.rate
		except: pass

		if not exchange_rate:
			try:
				exchange_rate = MyExchangeRate.objects.get(foreign=self.currency, home=vendor_item.currency)
				converted_cost = vendor_item.price * exchange_rate.rate
			except: pass
		if converted_cost: return self.price / converted_cost
		else: return None
	multiplier = property(_multiplier)

	def _total_physical(self):
		return sum(self.physical.values())
	total_physical = property(_total_physical)

	def _total_theoretical(self):
		return sum(self.theoretical.values())
	total_theoretical = property(_total_theoretical)

	def _physical(self):
		qty = {}
		for inv_item in MyItemInventory.objects.filter(item = self):
			if inv_item.withdrawable: qty[inv_item.size] = inv_item.physical
		return qty
	physical = property(_physical)

	def _theoretical(self):
		qty = {}
		for inv_item in MyItemInventory.objects.filter(item = self):
			qty[inv_item.size] = inv_item.theoretical
		return qty
	theoretical = property(_theoretical)

	def __unicode__(self):
		return u'%s | %s' %(self.name,self.color)

class MyItemInventory(models.Model):
	item = models.ForeignKey('MyItem')
	size = models.CharField(
		max_length = 4,
		default = ''
	)
	storage = models.ForeignKey('MyStorage')
	withdrawable = models.BooleanField(default = True)

	physical = models.IntegerField(default = 0)

	def _theoretical(self):
		inv = 0
		for audit in MyItemInventoryMoveAudit.objects.filter(inv = self):
			if audit.out: inv -= audit.qty
			else: inv += audit.qty
		return inv
	theoretical = property(_theoretical)

class MyItemInventoryMoveAudit(models.Model):
	created_on = models.DateField(auto_now_add = True)

	# instance fields
	created_by = models.ForeignKey (
		User,
		blank = True,
		null = True,
		default = None,
		verbose_name = u'创建用户',
		help_text = ''
	)

	# Against this inventory we are adjusting
	inv = models.ForeignKey('MyItemInventory')

	# If True, we are depleting qty.
	out = models.BooleanField(default = False)
	qty = models.IntegerField(default = 0)

	# Linked PO or SO
	so = models.ForeignKey(
		'MySalesOrderFullfillment',
		null = True,
		blank = True,
	)
	reason = models.TextField(default='')

class MySalesOrder(models.Model):
	supplier = models.ForeignKey('MyCRM', related_name='supplier')
	customer = models.ForeignKey('MyCRM', related_name='customer')
	created_on = models.DateField(auto_now_add = True)

	# instance fields
	created_by = models.ForeignKey (
		User,
		blank = True,
		null = True,
		default = None,
		verbose_name = u'创建用户',
		help_text = ''
	)
	discount = models.FloatField(default = 0)

class MySalesOrderLineItem(models.Model):
	order = models.ForeignKey('MySalesOrder')
	item = models.ForeignKey('MyItem')
	size = models.CharField(
		max_length = 4,
		default = ''
	)
	qty = models.IntegerField(default = 0)
	price = models.FloatField(default = 0)
	value = models.FloatField(default = 0)

	# This value will be updated whenever 
	# there is a new MySalesOrderFullfillmentLineItem created.
	fullfilled = models.IntegerField(default = 0)
	fullfill_rate = models.FloatField(default = 0)

class MyPurchaseOrder(MyBaseModel):
	'''
	Attachment will be invoice, packing list, shipment info.
	'''

	# There is always a SO linked to a PO!
	# For WH PO, we will still create a SO, using SH or SZ as client.
	# This enforces payment settlement between even internal parties.
	so = models.ForeignKey('MySalesOrder')
	vendor = models.ForeignKey('MyCRM')
	created_on = models.DateField(auto_now_add = True)

	# instance fields
	created_by = models.ForeignKey (
		User,
		blank = True,
		null = True,
		default = None,
		verbose_name = u'创建用户',
		help_text = ''
	)

class MyPurchaseOrderLineItem(models.Model):
	ESTIMATED_MONTH_CHOICES = (
		(u'UNKNOWN',u'UNKNOWN'),
		(u'LOCAL',u'LOCAL'),
		(u'NEVER',u'NEVER'),
		(u'JAN',u'JAN'),
		(u'FEB',u'FEB'),
		(u'MAR',u'MAR'),
		(U'APR',u'APR'),
		(U'MAY',u'MAY'),
		(U'JUN',u'JUN'),
		(U'JUL',u'JUL'),
		(U'AUG',u'AUG'),
		(U'SEP',u'SEP'),
		(U'OCT',u'OCT'),
		(U'NOV',u'NOV'),
		(U'DEC',u'DEC'),
	)
	po = models.ForeignKey('MyPurchaseOrder')
	so_line_item = models.ForeignKey('MySalesOrderLineItem')
	invoiced_qty = models.IntegerField(default = 0)
	packinglist_qty = models.IntegerField(default = 0)
	available_in = models.CharField(
		max_length = 8,
		null = True,
		blank = True,
		choices = ESTIMATED_MONTH_CHOICES
	)

class MySalesOrderFullfillment(MyBaseModel):
	'''
	Fullfillment would require an associated PO.
	'''
	so = models.ForeignKey('MySalesOrder')
	po = models.ForeignKey('MyPurchaseOrder')
	created_on = models.DateField(auto_now_add = True)
	created_by = models.ForeignKey (
		User,
		blank = True,
		null = True,
		default = None,
		verbose_name = u'创建用户',
		help_text = ''
	)

class MySalesOrderFullfillmentLineItem(models.Model):
	so_fullfillment = models.ForeignKey('MySalesOrderFullfillment')
	po_line_item = models.ForeignKey('MyPurchaseOrderLineItem')
	so_line_item = models.ForeignKey('MySalesOrderLineItem')
	fullfill_qty = models.IntegerField(default = 0)