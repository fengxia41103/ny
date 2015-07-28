from django.contrib import admin
from intern.models import *

# Register your models here.

class MyContactAdmin(admin.ModelAdmin):
	list_filter=['name',]
	list_display=('name','email',)
admin.site.register(MyExternalContact,MyContactAdmin)

class MyStatusAdmin(admin.ModelAdmin):
	list_display=('status','contact')
admin.site.register(MyStatus,MyStatusAdmin)

class MyApplicationAdmin(admin.ModelAdmin):
	list_display=('applicant_name','start_date','end_date','status')	
admin.site.register(MyApplication,MyApplicationAdmin)

admin.site.register(MySponsor)


class MyRoomAdmin(admin.ModelAdmin):
	list_display = ('name','tracking')
admin.site.register(MyRoom,MyRoomAdmin)

class MyBoxAdmin(admin.ModelAdmin):
	list_display = ('room','size','status','valuable_index')
	list_filter = ['room','size','valuable_index']
admin.site.register(MyBox,MyBoxAdmin)

class MyItemAdmin(admin.ModelAdmin):
	list_display = ('name','status')
	list_filter=['boxes','room']
admin.site.register(MyItem,MyItemAdmin)