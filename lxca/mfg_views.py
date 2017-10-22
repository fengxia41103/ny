import os
from django.conf import settings
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import FormView
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse

# django-filters
from django_filters import AllValuesFilter
from django_filters import BooleanFilter
from django_filters import FilterSet
from django_filters import ModelChoiceFilter
from django_filters.views import FilterView
from django_filters.widgets import LinkWidget

from lxca.forms import *
from lxca.models import *
from lxca.architect_models import *
from lxca.mfg_models import *

###################################################
#
#	 MFG solution views
#
###################################################


class MfgSolutionListFilter (FilterSet):

    class Meta:
        model = MfgSolution
        fields = ["order"]


class MfgSolutionList(FilterView):
    template_name = "lxca/solution/mfg_list.html"
    paginate_by = 10

    def get_filterset_class(self):
        return MfgSolutionListFilter


class MfgSolutionAdd(CreateView):
    model = MfgSolution
    template_name = 'common/add_form.html'
    success_url = reverse_lazy('mfg_solution_list')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['title'] = u'New Mfg'
        context['list_url'] = self.success_url
        context['objects'] = MfgSolution.objects.all()
        return context


class MfgSolutionDelete (DeleteView):
    model = MfgSolution
    template_name = 'common/delete_form.html'
    success_url = reverse_lazy('mfg_solution_list')

    def get_context_data(self, **kwargs):
        context = super(DeleteView, self).get_context_data(**kwargs)
        context['title'] = u'Delete Mfg'
        context['list_url'] = reverse_lazy('mfg_solution_list')
        return context


class MfgSolutionEdit(UpdateView):
    model = MfgSolution
    template_name = "common/edit_form.html"
    success_url = reverse_lazy("mfg_solution_list")

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['title'] = u'Edit Mfg'
        context['list_url'] = reverse_lazy('mfg_solution_list')
        return context


class MfgSolutionDetail(DetailView):
    model = MfgSolution
    template_name = "lxca/solution/mfg_detail.html"

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)

        # use MFG forms
        context["pdu_forms"] = [
            MfgPduForm(instance=i) for i in self.object.pdus.all()]
        context["switch_forms"] = [
            MfgSwitchForm(instance=i) for i in self.object.switches.all()]
        context["server_forms"] = [
            MfgServerForm(instance=i) for i in self.object.servers.all()]
        return context


def download_solution_bundle(request, pk):
    mfg = MfgSolution.objects.get(pk=int(pk))
    response = HttpResponse(mfg.yaml_bundle,
                            content_type='application/yaml')
    response['Content-Disposition'] = 'attachment; filename="bundle.yaml"'
    return response

###################################################
#
#	 Mfg RACK views
#
###################################################


class MfgRackListFilter (FilterSet):

    class Meta:
        model = MfgRack


class MfgRackList(FilterView):
    template_name = "lxca/rack/mfg_list.html"
    paginate_by = 10

    def get_filterset_class(self):
        return MfgRackListFilter


class MfgRackEdit(UpdateView):
    model = MfgRack
    template_name = "common/edit_form.html"
    form_class = MfgRackForm
    success_url = reverse_lazy("mfg_rack_list")

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['title'] = u'Edit MfgRack'
        context['list_url'] = reverse_lazy('mfg_solution_detail',
                                           kwargs={"pk": self.object.mfg.id})
        return context
###################################################
#
#	 Mfg PDU views
#
###################################################


class MfgPduListFilter (FilterSet):

    class Meta:
        model = MfgPdu


class MfgPduList(FilterView):
    template_name = "lxca/pdu/mfg_list.html"
    paginate_by = 10

    def get_filterset_class(self):
        return MfgPduListFilter


class MfgPduEdit(UpdateView):
    model = MfgPdu
    template_name = "common/edit_form.html"
    form_class = MfgPduForm
    success_url = reverse_lazy("mfg_pdu_list")

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['title'] = u'Edit MfgPdu'
        context['list_url'] = reverse_lazy('mfg_solution_detail',
                                           kwargs={"pk": self.object.mfg.id})
        return context

###################################################
#
#	 Mfg SWITCH views
#
###################################################


class MfgSwitchListFilter (FilterSet):

    class Meta:
        model = MfgSwitch


class MfgSwitchList(FilterView):
    template_name = "lxca/switch/mfg_list.html"
    paginate_by = 10

    def get_filterset_class(self):
        return MfgSwitchListFilter


class MfgSwitchEdit(UpdateView):
    model = MfgSwitch
    template_name = "common/edit_form.html"
    form_class = MfgSwitchForm
    success_url = reverse_lazy("mfg_switch_list")

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['title'] = u'Edit MfgSwitch'
        context['list_url'] = reverse_lazy('mfg_solution_detail',
                                           kwargs={"pk": self.object.mfg.id})
        return context

###################################################
#
#	 Mfg server views
#
###################################################


class MfgServerListFilter (FilterSet):

    class Meta:
        model = MfgServer
        fields = ["order__cores"]


class MfgServerList(FilterView):
    template_name = "lxca/server/mfg_list.html"
    paginate_by = 10

    def get_filterset_class(self):
        return MfgServerListFilter


class MfgServerEdit(UpdateView):
    model = MfgServer
    template_name = "common/edit_form.html"
    form_class = MfgServerForm
    success_url = reverse_lazy("mfg_server_list")

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['title'] = u'Edit MfgServer'
        context['list_url'] = reverse_lazy('mfg_solution_detail',
                                           kwargs={"pk": self.object.mfg.id})
        return context
