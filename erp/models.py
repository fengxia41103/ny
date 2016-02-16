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
	address = models.TextField(default='')
	users = models.ManyToManyField(User,null=True,blank=True)

	def _code(self):
		return u'%s-%s' %(self.crm,self.name)
	code = property(_code)

	def __unicode__(self):
		return self.code

class MyStorage (models.Model):
	location = models.ForeignKey('MyLocation')
	is_primary = models.BooleanField(default=True)

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
	currency = models.ForeignKey('MyCurrency')
	std_discount = models.FloatField(default=0.25)

	def __unicode__(self):
		return self.name
	
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

class MySizeChart(models.Model):
	# CSV format, eg "S,M,L", "0,2,4,6","XS,S,M,L,XL"
	size = models.CharField(
		max_length = 128
	)
	def __unicode__(self):
		return self.size

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
	price = models.FloatField(default = 0) # retail price
	currency = models.ForeignKey('MyCurrency')

	# If we know when is the deadline to place SO
	# against this item. This is observed when showing items
	# available for SO on e-Commerce site.
	order_deadline = models.DateField(
		null = True,
		blank = True,
	)

	# size chart
	size_chart = models.ForeignKey(
		'MySizeChart',
		null = True,
		blank = True
	)

	def _code(self):
		return u'%s-%s' %(self.name,self.color)
	code = property(_code)

	def _converted_cost(self):
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
		return converted_cost		
	converted_cost = property(_converted_cost)

	def _multiplier(self):
		if self.converted_cost: return self.price / self.converted_cost
		else: return None
	multiplier = property(_multiplier)

	def _total_physical(self):
		return sum([qty for size,qty in self.physical])
	total_physical = property(_total_physical)

	def _total_theoretical(self):
		return sum([qty for size,qty in self.theoretical])
	total_theoretical = property(_total_theoretical)

	def _physical(self):
		qty = []
		for inv_item in MyItemInventory.objects.filter(item = self):
			if inv_item.withdrawable: qty.append((inv_item.size,inv_item.physical))
		return qty
	physical = property(_physical)

	def _theoretical(self):
		qty = []
		for inv_item in MyItemInventory.objects.filter(item = self).order_by('size'):
			qty.append((inv_item.size,inv_item.theoretical))
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
	customer = models.ForeignKey('MyCRM')
	sales = models.ForeignKey(User, related_name='sales')
	default_storage = models.ForeignKey('MyStorage',null=True,blank=True)
	created_on = models.DateField(auto_now_add = True)

	# instance fields
	created_by = models.ForeignKey (
		User,
		blank = True,
		null = True,
		default = None,
		verbose_name = u'创建用户',
		help_text = '',
		related_name='logger'
	)
	discount = models.FloatField(default = 0)

	# Set this flag to True for internal customers.
	# This will force line item price to use item's converted cost instead of RP.
	is_sold_at_cost = models.BooleanField(default=False)

	# Order status
	STATUS_CHOICES = (
		('N','New'),
		('C','Closed'),
		('R','In Review'),
		('F','Fullfilling'),
	)
	status = models.CharField(
		max_length = 16,
		null = True,
		blank = True,
		default = 'N',
		choices = STATUS_CHOICES
	)

	def __unicode__(self):
		return u'%s, %s'%(self.code,self.customer)

	def _code(self):
		return '%s %d-%5d'%('SZ',dt.now().year,self.id)
	code = property(_code)

	def _life_in_days(self):
		return (dt.now()-self.created_on).days
	life_in_days = property(_life_in_days)

	def _line_item_qty(self):
		return len(MySalesOrderLineItem.objects.filter(order=self).values_list('id',flat=True))
	line_item_qty = property(_line_item_qty)

	def _total_qty(self):
		return sum(MySalesOrderLineItem.objects.filter(order=self).values_list('qty',flat=True))
	total_qty = property(_total_qty)

	def _total_std_value(self):
		vals = [line.std_value for line in MySalesOrderLineItem.objects.filter(order=self)]
		return sum(vals)
	total_std_value = property(_total_std_value)

	def _total_discount_value(self):
		vals = [line.discount_value for line in MySalesOrderLineItem.objects.filter(order=self)]
		return sum(vals)
	total_discount_value = property(_total_discount_value)

	def _implied_discount(self):
		return 1-self.total_discount_value/self.total_std_value
	implied_discount = property(_implied_discount)

	def _fullfill_qty(self):
		vals = [line.fullfill_qty for line in MySalesOrderLineItem.objects.filter(order=self)]
		return sum(vals)
	fullfill_qty = property(_fullfill_qty)

	def _fullfill_std_value(self):
		return sum([line.fullfill_qty*line.price for line in MySalesOrderLineItem.objects.filter(order=self)])
	fullfill_std_value = property(_fullfill_std_value)

	def _fullfill_discount_value(self):
		return sum([line.fullfill_qty*line.discount_value for line in MySalesOrderLineItem.objects.filter(order=self)])
	fullfill_discount_value = property(_fullfill_discount_value)

	def _fullfill_rate_by_qty(self):
		return self.fullfill_qty/self.total_qty
	fullfill_rate_by_qty = property(_fullfill_rate_by_qty)

	def _fullfill_rate_by_value(self):
		return self.fullfill_std_value / self.total_std_value
	fullfill_rate_by_value = property(_fullfill_rate_by_value)

	def _last_fullfill_date(self):
		return MySalesOrderFullfillment.objects.filter(so=self).order_by('-created_on')[0]
	last_fullfill_date = property(_last_fullfill_date)

	def _fullfillments(self):
		return MySalesOrderFullfillment.objects.filter(so=self).order_by('-created_on')
	fullfillments = property(_fullfillments)

class MySalesOrderLineItem(models.Model):
	order = models.ForeignKey('MySalesOrder')
	item = models.ForeignKey('MyItemInventory')
	qty = models.IntegerField(default = 0)

	# Price is a snapshot in time since xchange rate would fluctuate overtime.
	price = models.FloatField(default = 0)

	def _std_value(self):
		return self.qty*self.price
	std_value = property(_std_value)

	def _discount_price(self):
		return self.price*(1-self.order.discount)
	discount_price = property(_discount_price)

	def _discount_value(self):
		if self.order.is_sold_at_cost: return self.item.item.converted_cost
		else: return self.std_value * (1-self.order.discount)
	discount_value = property(_discount_value)

	def _fullfill_qty(self):
		qty=MySalesOrderFullfillmentLineItem.objects.filter(so_line_item=self).values('fullfill_qty',flat=True)
		return sum(qty)
	fullfill_qty = property(_fullfill_qty)

	def _fullfill_rate(self):
		return self.fullfill_qty/self.qty
	fullfill_rate = property(_fullfill_rate)

class MySalesOrderFullfillment(MyBaseModel):
	'''
	Fullfillment would require an associated PO.
	'''
	so = models.ForeignKey('MySalesOrder')
	po = models.ForeignKey(
		'MyPurchaseOrder',
		blank = True,
		null = True
	)
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
	po_line_item = models.ForeignKey(
		'MyPurchaseOrderLineItem',
		null = True,
		blank = True
	)
	so_line_item = models.ForeignKey('MySalesOrderLineItem')
	fullfill_qty = models.IntegerField(default = 0)

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

