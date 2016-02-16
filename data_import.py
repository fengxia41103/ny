#!/usr/bin/python  
# -*- coding: utf-8 -*- 
import sys,time,os,os.path,gc,csv
import lxml.html,codecs
import urllib,urllib2
import re
import simplejson as json

# setup Django
import django
sys.path.append(os.path.join(os.path.dirname(__file__), 'wei'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wei.settings")
from django.conf import settings

from django.utils import timezone

# import models
from erp.models import *

import xlrd, os.path
def import_fa_product():
	cur_rmb = MyCurrency.objects.get(abbrev = 'RMB')

	name = '/home/fengxia/Downloads/0_item_codes.xls'
	wk = xlrd.open_workbook(name)
	for s in wk.sheet_names():
		sheet = wk.sheet_by_name(s)
		for row in range(1,sheet.nrows):
			print 'processing', row

			# currency
			currency = sheet.cell(row,7).value
			currency, created = MyCurrency.objects.get_or_create(abbrev = currency.upper().strip())

			vendor = sheet.cell(row,1).value
			vendor,created = MyCRM.objects.get_or_create(name = vendor.upper().strip(),home_currency = currency)

			# parse season
			season = sheet.cell(row,2).value
			season = season.split('|')[1].strip()
			season, created = MySeason.objects.get_or_create(name = season.upper().strip())



			# parse desp
			desp = sheet.cell(row,10).value
			try:
				style = desp.split('\n')[0].split(':')[1].upper().strip()
				color = desp.split('\n')[1].split(':')[1].upper().strip()
				if '.' in color: color = color[:color.find('.')]
				size = desp.split('\n')[2].split(':')[1].upper().strip()
			except:
				print row

			# price always in RMB
			price = sheet.cell(row,6).value
			item,created= MyItem.objects.get_or_create(
				name = style,
				season = season,
				brand = vendor,
				color = color,
				price = price,
				currency = cur_rmb
			)
			item.save()

			cost = sheet.cell(row,9).value
			vendor_item,created = MyVendorItem.objects.get_or_create(
				vendor = vendor,
				product = item,
				price = cost,
				currency = vendor.home_currency
			)
			vendor_item.save()

def populate_item_inventory():
	storage = MyStorage.objects.get(id=1)
	for item in MyItem.objects.all():
		for size in item.size_chart.size.split(','):
			item_inv,created = MyItemInventory.objects.get_or_create(item=item,size=size,storage=storage)
		print item, 'done'

def main():
	django.setup()

	# import_fa_product()
	populate_item_inventory()
if __name__ == '__main__':
	main()
