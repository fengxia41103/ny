import os

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView
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

from lxca.catalog_models import *
from lxca.forms import *
from lxca.models import *

###################################################
#
#	Catalog rack views
#
###################################################


def CatalogRack_attachment_add(request, pk):
    tmp_form = AttachmentForm(request.POST, request.FILES)

    if tmp_form.is_valid():
        t = tmp_form.save(commit=False)
        t.name = request.FILES["file"].name
        t.content_object = CatalogRack.objects.get(id=pk)
        t.created_by = request.user
        t.save()
    return HttpResponseRedirect(
        reverse_lazy("catalog_rack_detail",
                     kwargs={"pk": pk}))


@login_required
def CatalogRack_attachment_delete(request, pk):
    a = Attachment.objects.get(id=pk)
    object_id = a.object_id

    # once we set MEDIA_ROOT, we will delete local file from file system also
    if os.path.exists(a.file.path):
        os.remove(os.path.join(settings.MEDIA_ROOT, a.file.path))

    # delete model
    a.delete()
    return HttpResponseRedirect(
        reverse_lazy("catalog_rack_detail",
                     kwargs={"pk": object_id}))


class CatalogRackListFilter (FilterSet):

    class Meta:
        model = CatalogRack
        fields = ["name", "eia_capacity"]


class CatalogRackList(FilterView):
    template_name = "lxca/rack/catalog_list.html"
    paginate_by = 10

    def get_filterset_class(self):
        return CatalogRackListFilter


class CatalogRackAdd(CreateView):
    model = CatalogRack
    template_name = 'common/add_form.html'
    success_url = reverse_lazy('catalog_rack_list')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['title'] = u'New Rack'
        context['list_url'] = self.success_url
        context['objects'] = CatalogRack.objects.all()
        return context


class CatalogRackDelete (DeleteView):
    model = CatalogRack
    template_name = 'common/delete_form.html'
    success_url = reverse_lazy('catalog_rack_list')

    def get_context_data(self, **kwargs):
        context = super(DeleteView, self).get_context_data(**kwargs)
        context['title'] = u'Delete item'
        context['list_url'] = reverse_lazy('catalog_rack_list')
        return context


class CatalogRackEdit(UpdateView):
    model = CatalogRack
    template_name = "common/edit_form.html"
    success_url = reverse_lazy("catalog_rack_list")

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['title'] = u'Edit Rack'
        context['list_url'] = reverse_lazy('catalog_rack_list')
        context['attachment_form'] = AttachmentForm()
        return context


class CatalogRackDetail(DetailView):
    model = CatalogRack
    template_name = "lxca/rack/catalog_detail.html"

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context["attachment_form"] = AttachmentForm()
        context["images"] = [
            img.file.url for img in self.object.attachments.all()]

        context['form'] = form = CatalogRackForm(instance=self.object)
        return context

###################################################
#
#	Catalog pdu views
#
###################################################


def CatalogPdu_attachment_add(request, pk):
    tmp_form = AttachmentForm(request.POST, request.FILES)

    if tmp_form.is_valid():
        t = tmp_form.save(commit=False)
        t.name = request.FILES["file"].name
        t.content_object = CatalogPdu.objects.get(id=pk)
        t.created_by = request.user
        t.save()
    return HttpResponseRedirect(
        reverse_lazy("catalog_pdu_detail",
                     kwargs={"pk": pk}))


@login_required
def CatalogPdu_attachment_delete(request, pk):
    a = Attachment.objects.get(id=pk)
    object_id = a.object_id

    # once we set MEDIA_ROOT, we will delete local file from file system also
    if os.path.exists(a.file.path):
        os.remove(os.path.join(settings.MEDIA_ROOT, a.file.path))

    # delete model
    a.delete()
    return HttpResponseRedirect(
        reverse_lazy("catalog_pdu_detail",
                     kwargs={"pk": object_id}))


class CatalogPduListFilter (FilterSet):

    class Meta:
        model = CatalogPdu
        fields = ["name", "c13", "c19", "is_monitored"]


class CatalogPduList(FilterView):
    template_name = "lxca/pdu/catalog_list.html"
    paginate_by = 10

    def get_filterset_class(self):
        return CatalogPduListFilter


class CatalogPduAdd(CreateView):
    model = CatalogPdu
    template_name = 'common/add_form.html'
    success_url = reverse_lazy('catalog_pdu_list')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['title'] = u'New PDU'
        context['list_url'] = self.success_url
        context['objects'] = CatalogPdu.objects.all()
        return context


class CatalogPduDelete (DeleteView):
    model = CatalogPdu
    template_name = 'common/delete_form.html'
    success_url = reverse_lazy('catalog_pdu_list')

    def get_context_data(self, **kwargs):
        context = super(DeleteView, self).get_context_data(**kwargs)
        context['title'] = u'Delete item'
        context['list_url'] = reverse_lazy('catalog_pdu_list')
        return context


class CatalogPduEdit(UpdateView):
    model = CatalogPdu
    template_name = "common/edit_form.html"
    success_url = reverse_lazy("catalog_pdu_list")

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['title'] = u'Edit PDU'
        context['list_url'] = reverse_lazy('catalog_pdu_list')
        context['attachment_form'] = AttachmentForm()
        return context


class CatalogPduDetail(DetailView):
    model = CatalogPdu
    template_name = "lxca/pdu/catalog_detail.html"

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context["attachment_form"] = AttachmentForm()
        context["images"] = [
            img.file.url for img in self.object.attachments.all()]
        return context

###################################################
#
#	Catalog switch views
#
###################################################


def CatalogSwitch_attachment_add(request, pk):
    tmp_form = AttachmentForm(request.POST, request.FILES)

    if tmp_form.is_valid():
        t = tmp_form.save(commit=False)
        t.name = request.FILES["file"].name
        t.content_object = CatalogSwitch.objects.get(id=pk)
        t.created_by = request.user
        t.save()
    return HttpResponseRedirect(
        reverse_lazy("catalog_switch_detail",
                     kwargs={"pk": pk}))


@login_required
def CatalogSwitch_attachment_delete(request, pk):
    a = Attachment.objects.get(id=pk)
    object_id = a.object_id

    # once we set MEDIA_ROOT, we will delete local file from file system also
    if os.path.exists(a.file.path):
        os.remove(os.path.join(settings.MEDIA_ROOT, a.file.path))

    # delete model
    a.delete()
    return HttpResponseRedirect(
        reverse_lazy("catalog_switch_detail",
                     kwargs={"pk": object_id}))


class CatalogSwitchListFilter (FilterSet):

    class Meta:
        model = CatalogSwitch
        fields = ["name", "speed", "rear_to_front"]


class CatalogSwitchList(FilterView):
    template_name = "lxca/switch/catalog_list.html"
    paginate_by = 10

    def get_filterset_class(self):
        return CatalogSwitchListFilter


class CatalogSwitchAdd(CreateView):
    model = CatalogSwitch
    template_name = 'common/add_form.html'
    success_url = reverse_lazy('catalog_switch_list')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['title'] = u'New Switch'
        context['list_url'] = self.success_url
        context['objects'] = CatalogSwitch.objects.all()
        return context


class CatalogSwitchDelete (DeleteView):
    model = CatalogSwitch
    template_name = 'common/delete_form.html'
    success_url = reverse_lazy('catalog_switch_list')

    def get_context_data(self, **kwargs):
        context = super(DeleteView, self).get_context_data(**kwargs)
        context['title'] = u'Delete item'
        context['list_url'] = reverse_lazy('catalog_switch_list')
        return context


class CatalogSwitchEdit(UpdateView):
    model = CatalogSwitch
    template_name = "common/edit_form.html"
    success_url = reverse_lazy("catalog_switch_list")

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['title'] = u'Edit Switch'
        context['list_url'] = reverse_lazy('catalog_switch_list')
        context['attachment_form'] = AttachmentForm()
        return context


class CatalogSwitchDetail(DetailView):
    model = CatalogSwitch
    template_name = "lxca/switch/catalog_detail.html"

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context["attachment_form"] = AttachmentForm()
        context["images"] = [
            img.file.url for img in self.object.attachments.all()]
        return context

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
