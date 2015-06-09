from django.contrib import admin
from intern.models import *

# Register your models here.

class MyContactAdmin(admin.ModelAdmin):
	list_filter=['name',]
	list_display=('name','email','phone')
admin.site.register(MyExternalContact,MyContactAdmin)

class MyStatusAdmin(admin.ModelAdmin):
	list_display=('status','contact')
admin.site.register(MyStatus,MyStatusAdmin)

class MyApplicationAdmin(admin.ModelAdmin):
	list_display=('applicant_name','start_date','end_date','status')	
admin.site.register(MyApplication,MyApplicationAdmin)