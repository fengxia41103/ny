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
from django.http import HttpResponseRedirect

# django-filters
from django_filters import AllValuesFilter
from django_filters import BooleanFilter
from django_filters import FilterSet
from django_filters import ModelChoiceFilter
from django_filters.views import FilterView
from django_filters.widgets import LinkWidget

from lxca.forms import *
from lxca.models import *
from lxca.order_models import *

###################################################
#
#	 Order solution views
#
###################################################


class OrderSolutionListFilter (FilterSet):

    class Meta:
        model = OrderSolution
        fields = ["order", "status"]


class OrderSolutionList(FilterView):
    template_name = "lxca/solution/order_list.html"
    paginate_by = 10

    def get_filterset_class(self):
        return OrderSolutionListFilter


class OrderSolutionAdd(CreateView):
    model = OrderSolution
    template_name = 'common/add_form.html'
    success_url = reverse_lazy('order_solution_list')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['title'] = u'New Order'
        context['list_url'] = self.success_url
        context['objects'] = OrderSolution.objects.all()
        return context


class OrderSolutionDelete (DeleteView):
    model = OrderSolution
    template_name = 'common/delete_form.html'
    success_url = reverse_lazy('order_solution_list')

    def get_context_data(self, **kwargs):
        context = super(DeleteView, self).get_context_data(**kwargs)
        context['title'] = u'Delete Order'
        context['list_url'] = reverse_lazy('order_solution_list')
        return context


class OrderSolutionEdit(UpdateView):
    model = OrderSolution
    template_name = "common/edit_form.html"
    success_url = reverse_lazy("order_solution_list")

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['title'] = u'Edit Order'
        context['list_url'] = reverse_lazy('order_solution_list')
        return context


class OrderSolutionDetail(DetailView):
    model = OrderSolution
    template_name = "lxca/solution/order_detail.html"

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context["pdu_forms"] = [
            OrderPduForm(instance=i) for i in self.object.pdus.all()]
        context["switch_forms"] = [
            OrderSwitchForm(instance=i) for i in self.object.switches.all()]
        context["server_forms"] = [
            OrderServerForm(instance=i) for i in self.object.servers.all()]
        return context

###################################################
#
#	 Order PDU views
#
###################################################


class OrderPduListFilter (FilterSet):

    class Meta:
        model = OrderPdu


class OrderPduList(FilterView):
    template_name = "lxca/pdu/order_list.html"
    paginate_by = 10

    def get_filterset_class(self):
        return OrderPduListFilter


class OrderPduEdit(UpdateView):
    model = OrderPdu
    template_name = "common/edit_form.html"
    form_class = OrderPduForm
    success_url = reverse_lazy("order_pdu_list")

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['title'] = u'Edit OrderPdu'
        context['list_url'] = reverse_lazy('order_solution_detail',
                                           kwargs={"pk": self.object.order.id})
        return context

###################################################
#
#	 Order SWITCH views
#
###################################################


class OrderSwitchListFilter (FilterSet):

    class Meta:
        model = OrderSwitch


class OrderSwitchList(FilterView):
    template_name = "lxca/switch/order_list.html"
    paginate_by = 10

    def get_filterset_class(self):
        return OrderSwitchListFilter


class OrderSwitchEdit(UpdateView):
    model = OrderSwitch
    template_name = "common/edit_form.html"
    form_class = OrderSwitchForm
    success_url = reverse_lazy("order_switch_list")

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['title'] = u'Edit OrderSwitch'
        context['list_url'] = reverse_lazy('order_solution_detail',
                                           kwargs={"pk": self.object.order.id})
        return context

###################################################
#
#	 Order server views
#
###################################################


class OrderServerListFilter (FilterSet):

    class Meta:
        model = OrderServer
        fields = ["firmware", "cores", "mem"]


class OrderServerList(FilterView):
    template_name = "lxca/server/order_list.html"
    paginate_by = 10

    def get_filterset_class(self):
        return OrderServerListFilter


class OrderServerEdit(UpdateView):
    model = OrderServer
    template_name = "common/edit_form.html"
    form_class = OrderServerForm
    success_url = reverse_lazy("order_server_list")

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['title'] = u'Edit OrderServer'
        context['list_url'] = reverse_lazy('order_solution_detail',
                                           kwargs={"pk": self.object.order.id})
        return context
