from django.contrib import admin
from erp.models import *

# Register your models here.

class MyCountryAdmin(admin.ModelAdmin):
	list_filter=['name','abbrev']
	list_display=('name','abbrev',)
admin.site.register(MyCountry,MyCountryAdmin)

class MyCurrencyAdmin(admin.ModelAdmin):
	list_filter=['name','abbrev','country']
	list_display=('name','abbrev','symbol')
admin.site.register(MyCurrency,MyCurrencyAdmin)

class MyCompanyAdmin(admin.ModelAdmin):
	list_filter=['name','abbrev']
admin.site.register(MyCompany,MyCompanyAdmin)

class MyExchangeRateAdmin(admin.ModelAdmin):
	list_filter=['home','foreign','rate']
admin.site.register(MyExchangeRate,MyExchangeRateAdmin)

admin.site.register(MyUOM)
admin.site.register(MyFiscalYear)
admin.site.register(MyStorage)
admin.site.register(MyLocation)
admin.site.register(MyCRM)
admin.site.register(MyVendorItem)
admin.site.register(MySeason)
admin.site.register(MyItem)
admin.site.register(MyItemInventory)
admin.site.register(MySalesOrder)
admin.site.register(MySalesOrderLineItem)
admin.site.register(MyPurchaseOrder)
admin.site.register(MyPurchaseOrderLineItem)
admin.site.register(MySalesOrderFullfillment)
admin.site.register(MySalesOrderFullfillmentLineItem)
