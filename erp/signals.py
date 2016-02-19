from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from erp.models import *

@receiver(pre_save, sender=MySizeChart)
def mysizechart_pre_save_hanelder(sender, instance, **kwargs):
	instance.size = instance.size.upper()

@receiver(post_save, sender=MyItem)
def myitem_post_save_handler(sender, instance, created, **kwargs):
	# Create MyVendorItem
	vendor_item,created = MyVendorItem.objects.get_or_create(
		vendor = instance.brand,
		currency = instance.brand.currency,
		product = instance
	)

@receiver(pre_save, sender=MyItem)
def myitem_pre_save_handler(sender, instance, **kwargs):
	try:
		obj = sender.objects.get(pk=instance.pk)
	except sender.DoesNotExist:
		pass # Object is new, so field hasn't technically changed, but you may want to do something else here.
	else:
		if not obj.size_chart == instance.size_chart: # Field has changed
			old_chart = obj.size_chart.size.split(',')
			new_chart = instance.size_chart.size.split(',')

			# We are swapping size chart, eg SML -> 2,4,6
			# Size chart should always be 5 levels!
			if len(old_chart) == len(new_chart):
				for (old_size,new_size) in zip(old_chart,new_chart):
					for item_inv in MyItemInventory.objects.filter(item=instance,size=old_size):
						item_inv.size = new_size
						item_inv.save()
			elif not obj.size_chart: # is None, creating ItemInventory
				# Location and Storage
				location = MyLocation.objects.filter(crm = instance.brand)			
				if len(location): location = location[0]
				else: 
					# Get location
					location = MyLocation(crm=instance.brand)
					location.save()

				# Create a storage
				storage, created = MyStorage.objects.get_or_create(location=location,is_primary=True)
				
				# Create MyItemInventory			
				for new_size in new_chart:
					MyItemInventory(
						item = instance,
						size = new_size,
						storage = storage
					).save()

@receiver(pre_save, sender=MyBusinessModel)
def mybusinessmodel_pre_save_handler(sender, instance, **kwargs):
	instance.name = instance.name.upper()	