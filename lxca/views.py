#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs
import csv
import hashlib
import os
import os.path
import random
# so what
import re
import shutil
import subprocess
import tempfile
import time
import unittest
import urllib
from datetime import datetime as dt
from itertools import groupby

import lxml.html
import simplejson as json
import testtools
# django-crispy-forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.contenttypes.generic import generic_inlineformset_factory
# django emails
from django.core.mail import send_mail
from django.core.urlresolvers import resolve
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.db.models import Avg
from django.db.models import Count
from django.db.models import Max
from django.db.models import Min
from django.db.models import Q
from django.forms.models import inlineformset_factory
from django.forms.models import modelformset_factory
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import Context
from django.template import RequestContext
from django.template import loader
from django.utils.decorators import method_decorator
from django.utils.encoding import smart_text
from django.views.decorators.csrf import csrf_exempt
# protect the view with require_POST decorator
from django.views.decorators.http import require_POST
from django.views.decorators.vary import vary_on_headers
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import FormView
from django.views.generic.edit import UpdateView
# django-filters
from django_filters import AllValuesFilter
from django_filters import BooleanFilter
from django_filters import FilterSet
from django_filters import ModelChoiceFilter
from django_filters.views import FilterView
from django_filters.widgets import LinkWidget

from lxca.forms import *
from lxca.models import *
from utility import MyUtility


###################################################
#
#	Common utilities
#
###################################################


def class_view_decorator(function_decorator):
    """Convert a function based decorator into a class based decorator usable
    on class based Views.

    Can"t subclass the `View` as it breaks inheritance (super in particular),
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
    template_name = "home/home_with_login_modal.html"

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)

        user_auth_form = AuthenticationForm()
        user_registration_form = UserCreationForm()

        context["registration_form"] = user_registration_form
        context["auth_form"] = user_auth_form
        return context

###################################################
#
#	User views
#
###################################################


class LoginView(FormView):
    template_name = "registration/login.html"
    success_url = reverse_lazy("catalog_server_list")
    form_class = AuthenticationForm

    def form_valid(self, form):
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)


class LogoutView(TemplateView):
    template_name = "registration/logged_out.html"

    def get(self, request):
        logout(request)
    # Redirect to a success page.
        # messages.add_message(request, messages.INFO, "Thank you for using our
        # service. Hope to see you soon!")
        return HttpResponseRedirect(reverse_lazy("home"))


class UserRegisterView(FormView):
    template_name = "registration/register_form.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user_name = form.cleaned_data["username"]
        password = form.cleaned_data["password2"]
        if len(User.objects.filter(username=user_name)) > 0:
            return self.form_invalid(form)
        else:
            user = User.objects.create_user(user_name, "", password)
            user.save()

            return super(UserRegisterView, self).form_valid(form)


###################################################
#
#	Catalog server views
#
###################################################

def CatalogServer_attachment_add(request, pk):
    tmp_form = AttachmentForm(request.POST, request.FILES)

    if tmp_form.is_valid():
        t = tmp_form.save(commit=False)
        t.name = request.FILES["file"].name
        t.content_object = CatalogServer.objects.get(id=pk)
        t.created_by = request.user
        t.save()
    return HttpResponseRedirect(
        reverse_lazy("catalog_server_detail",
                     kwargs={"pk": pk}))


@login_required
def CatalogServer_attachment_delete(request, pk):
    a = Attachment.objects.get(id=pk)
    object_id = a.object_id

    # once we set MEDIA_ROOT, we will delete local file from file system also
    if os.path.exists(a.file.path):
        os.remove(os.path.join(settings.MEDIA_ROOT, a.file.path))

    # delete model
    a.delete()
    return HttpResponseRedirect(
        reverse_lazy("catalog_server_detail",
                     kwargs={"pk": object_id}))


class CatalogServerListFilter (FilterSet):

    class Meta:
        model = CatalogServer
        fields = {
            "name": ["contains"],
            "size": ["exact"],
            "cpu_sockets": ["gt"]
        }


class CatalogServerList(FilterView):
    template_name = "lxca/server/catalog_list.html"
    paginate_by = 10

    def get_filterset_class(self):
        return CatalogServerListFilter


class CatalogServerAdd(CreateView):
    model = CatalogServer
    template_name = 'common/add_form.html'
    success_url = reverse_lazy('catalog_server_list')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['title'] = u'New Server'
        context['list_url'] = self.success_url
        context['objects'] = CatalogServer.objects.all()
        return context


class CatalogServerDelete (DeleteView):
    model = CatalogServer
    template_name = 'common/delete_form.html'
    success_url = reverse_lazy('catalog_server_list')

    def get_context_data(self, **kwargs):
        context = super(DeleteView, self).get_context_data(**kwargs)
        context['title'] = u'Delete item'
        context['list_url'] = reverse_lazy('catalog_server_list')
        return context


class CatalogServerEdit(UpdateView):
    model = CatalogServer
    template_name = "common/edit_form.html"
    success_url = reverse_lazy("catalog_server_list")

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['title'] = u'Edit Server'
        context['list_url'] = reverse_lazy('catalog_server_list')
        context['attachment_form'] = AttachmentForm()
        return context


class CatalogServerDetail(DetailView):
    model = CatalogServer
    template_name = "lxca/server/catalog_detail.html"

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context["attachment_form"] = AttachmentForm()
        context["images"] = [
            img.file.url for img in self.object.attachments.all()]
        return context

###################################################
#
#	 Architect solution views
#
###################################################


def ArchitectSolution_attachment_add(request, pk):
    tmp_form = AttachmentForm(request.POST, request.FILES)

    if tmp_form.is_valid():
        t = tmp_form.save(commit=False)
        t.name = request.FILES["file"].name
        t.content_object = ArchitectSolution.objects.get(id=pk)
        t.created_by = request.user
        t.save()
    return HttpResponseRedirect(
        reverse_lazy("sa_solution_detail",
                     kwargs={"pk": pk}))


@login_required
def ArchitectSolution_attachment_delete(request, pk):
    a = Attachment.objects.get(id=pk)
    object_id = a.object_id

    # once we set MEDIA_ROOT, we will delete local file from file system also
    if os.path.exists(a.file.path):
        os.remove(os.path.join(settings.MEDIA_ROOT, a.file.path))

    # delete model
    a.delete()
    return HttpResponseRedirect(
        reverse_lazy("sa_solution_detail",
                     kwargs={"pk": object_id}))


class ArchitectSolutionListFilter (FilterSet):

    class Meta:
        model = ArchitectSolution
        fields = ["name", "version"]


class ArchitectSolutionList(FilterView):
    template_name = "lxca/solution/sa_list.html"
    paginate_by = 10

    def get_filterset_class(self):
        return ArchitectSolutionListFilter


class ArchitectSolutionAdd(CreateView):
    model = ArchitectSolution
    template_name = 'common/add_form.html'
    success_url = reverse_lazy('sa_solution_list')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['title'] = u'New Solution'
        context['list_url'] = self.success_url
        context['objects'] = ArchitectSolution.objects.all()
        return context


class ArchitectSolutionDelete (DeleteView):
    model = ArchitectSolution
    template_name = 'common/delete_form.html'
    success_url = reverse_lazy('sa_solution_list')

    def get_context_data(self, **kwargs):
        context = super(DeleteView, self).get_context_data(**kwargs)
        context['title'] = u'Delete item'
        context['list_url'] = reverse_lazy('sa_solution_list')
        return context


class ArchitectSolutionEdit(UpdateView):
    model = ArchitectSolution
    template_name = "common/edit_form.html"
    success_url = reverse_lazy("sa_solution_list")

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['title'] = u'Edit Solution'
        context['list_url'] = reverse_lazy('sa_solution_list')
        context['attachment_form'] = AttachmentForm()
        return context


class ArchitectSolutionDetail(DetailView):
    model = ArchitectSolution
    template_name = "lxca/solution/sa_detail.html"

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context["attachment_form"] = AttachmentForm()
        context["images"] = [
            img.file.url for img in self.object.attachments.all()]
        return context
