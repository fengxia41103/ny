#!/usr/bin/python  
# -*- coding: utf-8 -*-  

from django import forms
from django.conf import settings
from django.forms.models import modelformset_factory, inlineformset_factory
from django.contrib.contenttypes.generic import generic_inlineformset_factory
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, logout, login
from django.template import RequestContext
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy, resolve, reverse
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, JsonResponse
from django.utils.encoding import smart_text
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count,Max,Min,Avg

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.vary import vary_on_headers
# protect the view with require_POST decorator
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.db.models import Q
from django.template import loader, Context

# django-crispy-forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

# django-filters
from django_filters import FilterSet, BooleanFilter,ModelChoiceFilter,AllValuesFilter
from django_filters.views import FilterView
from django_filters.widgets import LinkWidget

# django emails
from django.core.mail import send_mail

# so what
import re,os,os.path,shutil,subprocess, testtools
import random,codecs,unittest,time, tempfile, csv, hashlib
from datetime import datetime as dt
import simplejson as json
from itertools import groupby
import urllib, lxml.html
from utility import MyUtility

from erp.models import *
from erp.forms import *

###################################################
#
#	Common utilities
#
###################################################
def class_view_decorator(function_decorator):
	"""Convert a function based decorator into a class based decorator usable
	on class based Views.
	
	Can't subclass the `View` as it breaks inheritance (super in particular),
	so we monkey-patch instead.
	"""
	
	def simple_decorator(View):
		View.dispatch = method_decorator(function_decorator)(View.dispatch)
		return View
	
	return simple_decorator

###################################################
#
#	Static views
#
###################################################
class HomeView (TemplateView):
	template_name = 'erp/common/home_with_login_modal.html'

	def get_context_data(self, **kwargs):
		context = super(TemplateView, self).get_context_data(**kwargs)

		user_auth_form = AuthenticationForm()
		user_registration_form = UserCreationForm()

		context['registration_form']=user_registration_form
		context['auth_form']=user_auth_form
		return context

###################################################
#
#	User views
#
###################################################
class LoginView(FormView):
	template_name = 'registration/login.html'
	success_url = reverse_lazy('item_list')
	form_class = AuthenticationForm
	def form_valid(self,form):
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(username=username, password=password)

		if user is not None and user.is_active:
		    login(self.request, user)
		    return super(LoginView, self).form_valid(form)
		else:
		    return self.form_invalid(form)

class LogoutView(TemplateView):
	template_name = 'registration/logged_out.html'
	def get(self,request):
		logout(request)
    	# Redirect to a success page.
		# messages.add_message(request, messages.INFO, 'Thank you for using our service. Hope to see you soon!')
		return HttpResponseRedirect (reverse_lazy('home'))

class UserRegisterView(FormView):
	template_name = 'registration/register_form.html'
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	def form_valid(self,form):
		user_name = form.cleaned_data['username']
		password = form.cleaned_data['password2']
		if len(User.objects.filter(username = user_name))>0:
			return self.form_invalid(form)
		else:
			user = User.objects.create_user(user_name, '', password)			
			user.save()

			return super(UserRegisterView,self).form_valid(form)

###################################################
#
#	Attachment views
#
###################################################
@login_required
def attachment_delete_view(request,pk):
	a = Attachment.objects.get(id=pk)
	
	# once we set MEDIA_ROOT, we will delete local file from file system also
	if os.path.exists(a.file.path): os.remove(os.path.join(settings.MEDIA_ROOT,a.file.path))
	
	# delete model
	a.delete()
	return HttpResponseRedirect(reverse_lazy('item_list'))

def item_attachment_add_view(request, pk):
	tmp_form = AttachmentForm (request.POST, request.FILES)

	if tmp_form.is_valid():
		t=tmp_form.save(commit=False)
		t.name = 'something'
		t.content_object = MyItem.objects.get(id=pk)
		t.created_by = request.user
		t.save()	
	return HttpResponseRedirect("")

###################################################
#
#	MyApplication views
#
###################################################
class MyFiscalYearList(ListView):
	model = MyFiscalYear
	template_name = 'erp/fiscalyear/list.html'
	paginate_by = 10

class MyFiscalYearAdd(CreateView):
	model = MyFiscalYear
	template_name = 'erp/fiscalyear/add.html'
	success_url = reverse_lazy('fiscalyear_list')	
	def get_context_data(self, **kwargs):
		context = super(CreateView, self).get_context_data(**kwargs)
		context['title'] = u'New fiscal year'
		context['list_url'] = self.success_url
		context['objects'] = MyFiscalYear.objects.all()
		return context

@class_view_decorator(login_required)
class MyFiscalYearDelete (DeleteView):
	model = MyItem
	template_name = 'erp/common/delete_form.html'
	success_url = reverse_lazy('fiscalyear_list')

	def get_context_data(self, **kwargs):
		context = super(DeleteView, self).get_context_data(**kwargs)
		context['title'] = u'Delete fiscal year'
		context['list_url'] = reverse_lazy('fiscalyear_list')
		return context	

class MyItemAdd(CreateView):
	model = MyItem
	template_name = 'erp/common/add_form.html'
	success_url = reverse_lazy('item_list')
	fields = ['brand','season','name','color','price']	

	def form_valid(self, form):
		form.instance.created_by = self.request.user

		currency,created = MyCurrency.objects.get_or_create(abbrev='RMB')
		form.instance.currency = currency
		return super(CreateView, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(CreateView, self).get_context_data(**kwargs)
		context['title'] = u'New item'
		context['list_url'] = self.success_url
		return context

@class_view_decorator(login_required)
class MyItemEdit (UpdateView):
	model = MyItem
	template_name = 'erp/common/edit_form.html'
	
	def get_success_url(self):
		return reverse_lazy('item_detail', kwargs={'pk':self.get_object().id})
			
	def get_context_data(self, **kwargs):
		context = super(UpdateView, self).get_context_data(**kwargs)
		context['title'] = u'Edit item'
		context['list_url'] = reverse_lazy('item_list')
		return context

@class_view_decorator(login_required)
class MyItemDelete (DeleteView):
	model = MyItem
	template_name = 'erp/common/delete_form.html'
	success_url = reverse_lazy('item_list')

	def get_context_data(self, **kwargs):
		context = super(DeleteView, self).get_context_data(**kwargs)
		context['title'] = u'Delete item'
		context['list_url'] = reverse_lazy('item_list')
		return context		

class MyItemListFilter (FilterSet):
	brand = ModelChoiceFilter(queryset=MyCRM.objects.filter(crm_type='V').order_by('name'),widget=LinkWidget)
	season = ModelChoiceFilter(queryset=MySeason.objects.all().order_by('name'),widget=LinkWidget)

	class Meta:
		model = MyItem
		fields = ['brand','season','name']
		order_by = ['brand']
		together = ['season']

class MyItemList (FilterView):
	template_name = 'erp/item/list.html'
	paginate_by = 25

	def get_context_data(self, **kwargs):
		context = super(FilterView, self).get_context_data(**kwargs)
		searches = context['filter']
		context['filters'] = {} # my customized filter display values

		for f,val in searches.data.iteritems():
			if val and f != "csrfmiddlewaretoken" and f != "page":
				if f == 'brand': context['filters']['brand'] = MyCRM.objects.get(id=int(val))
				if f == 'season': context['filters']['season'] = MySeason.objects.get(id=int(val))
				if 'name' in f: context['filters']['name__contains'] = val
		return context		

	def get_filterset_class(self):
		return MyItemListFilter

class MyItemDetail(DetailView):
	model = MyItem
	template_name = 'erp/item/detail.html'

	def get_context_data(self, **kwargs):
		context = super(DetailView, self).get_context_data(**kwargs)
		context['attachment_form'] = AttachmentForm()
		context['images'] = [img.file.url for img in self.object.attachments.all()]
		return context
