# forms.py
from django import forms
from django.forms import ModelForm
from django.forms.widgets import HiddenInput
from erp.models import *

class AttachmentForm(ModelForm):
	class Meta:
		model = Attachment
		fields = ['description','file']

class ItemInventoryAdjustForm(forms.Form):
	storage = forms.ModelChoiceField(queryset=MyStorage.objects.all())
	items = forms.CharField(
		widget=forms.Textarea,
		help_text = u'''Put one item per line, using syntax <span class="item-label">style #, color, size-qty</span>. 
		You can also use item's SKU instead of its style # for convenience. Both style # field and color field would be
		used for partial matching so that you don't have to type in the entire string as they are shown on clothes tag. 
		To enter size and qty, use syntax "S-1, M-2". This field is case insensitive.
		'''
	)

class ItemInventoryAddForm(ItemInventoryAdjustForm):
	# Reason
	REASON_CHOICES = (
		('INITIAL','Qty is being adjusted as part of initial setup.'),
	)
	reason = forms.ChoiceField(choices = REASON_CHOICES)

class SalesOrderAddForm(forms.Form):
	customer = forms.ModelChoiceField(queryset=MyCRM.objects.filter(Q(crm_type='C')|Q(crm_type='B')))
	sales = forms.ModelChoiceField(
		queryset = User.objects.all(),
		label = u'Sales'
	)
	storage = forms.ModelChoiceField(
		queryset = MyStorage.objects.all(),
		label = u'Default fullfiller'
	)
	is_sold_at_cost = forms.BooleanField(
		initial=False,
		required=False,
		label= u'Are items sold at cost?'
	)
	customer_discount = forms.FloatField(initial=0.25)
	items = forms.CharField(
		widget=forms.Textarea,
		help_text = u'''Put one item per line, using syntax <span class="item-label">SKU #, color, size-qty</span>. 
		Color field would be
		used for partial matching so that you don't have to type in the entire string as they are shown on clothes tag. 
		To enter size and qty, use syntax "S-1, M-2". This field is case insensitive.
		'''
	)

class VendorItemForm(ModelForm):
	class Meta:
		model = MyVendorItem
		