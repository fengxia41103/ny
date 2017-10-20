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
from lxca.architect_models import *


###################################################
#
#	 Playbook views
#
###################################################

class PlaybookListFilter (FilterSet):

    class Meta:
        model = Playbook
        fields = ["for_type", "name", "path", "tags"]


class PlaybookList(FilterView):
    template_name = "lxca/playbook/sa_list.html"
    paginate_by = 10

    def get_filterset_class(self):
        return PlaybookListFilter


class PlaybookAdd(CreateView):
    model = Playbook
    template_name = 'common/add_form.html'
    success_url = reverse_lazy('sa_playbook_list')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['title'] = u'New Playbook'
        context['list_url'] = self.success_url
        context['objects'] = Playbook.objects.all()
        return context


class PlaybookDelete (DeleteView):
    model = Playbook
    template_name = 'common/delete_form.html'
    success_url = reverse_lazy('sa_playbook_list')

    def get_context_data(self, **kwargs):
        context = super(DeleteView, self).get_context_data(**kwargs)
        context['title'] = u'Delete item'
        context['list_url'] = reverse_lazy('sa_playbook_list')
        return context


class PlaybookEdit(UpdateView):
    model = Playbook
    template_name = "common/edit_form.html"
    success_url = reverse_lazy("sa_playbook_list")

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['title'] = u'Edit Playbook'
        context['list_url'] = reverse_lazy('sa_playbook_list')
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

###################################################
#
#	 Architect application views
#
###################################################


def ArchitectApplication_attachment_add(request, pk):
    tmp_form = AttachmentForm(request.POST, request.FILES)

    if tmp_form.is_valid():
        t = tmp_form.save(commit=False)
        t.name = request.FILES["file"].name
        t.content_object = ArchitectApplication.objects.get(id=pk)
        t.created_by = request.user
        t.save()
    return HttpResponseRedirect(
        reverse_lazy("sa_application_detail",
                     kwargs={"pk": pk}))


@login_required
def ArchitectApplication_attachment_delete(request, pk):
    a = Attachment.objects.get(id=pk)
    object_id = a.object_id

    # once we set MEDIA_ROOT, we will delete local file from file system also
    if os.path.exists(a.file.path):
        os.remove(os.path.join(settings.MEDIA_ROOT, a.file.path))

    # delete model
    a.delete()
    return HttpResponseRedirect(
        reverse_lazy("sa_application_detail",
                     kwargs={"pk": object_id}))


class ArchitectApplicationListFilter (FilterSet):

    class Meta:
        model = ArchitectApplication
        fields = ["name", "host"]


class ArchitectApplicationList(FilterView):
    template_name = "lxca/application/sa_list.html"
    paginate_by = 10

    def get_filterset_class(self):
        return ArchitectApplicationListFilter


class ArchitectApplicationAdd(CreateView):
    model = ArchitectApplication
    template_name = 'common/add_form.html'
    success_url = reverse_lazy('sa_application_list')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['title'] = u'New Application'
        context['list_url'] = self.success_url
        context['objects'] = ArchitectApplication.objects.all()
        return context


class ArchitectApplicationDelete (DeleteView):
    model = ArchitectApplication
    template_name = 'common/delete_form.html'
    success_url = reverse_lazy('sa_application_list')

    def get_context_data(self, **kwargs):
        context = super(DeleteView, self).get_context_data(**kwargs)
        context['title'] = u'Delete item'
        context['list_url'] = reverse_lazy('sa_application_list')
        return context


class ArchitectApplicationEdit(UpdateView):
    model = ArchitectApplication
    template_name = "common/edit_form.html"
    success_url = reverse_lazy("sa_application_list")

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['title'] = u'Edit Application'
        context['list_url'] = reverse_lazy('sa_application_list')
        context['attachment_form'] = AttachmentForm()
        return context


class ArchitectApplicationDetail(DetailView):
    model = ArchitectApplication
    template_name = "lxca/application/sa_detail.html"

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context["attachment_form"] = AttachmentForm()
        context["images"] = [
            img.file.url for img in self.object.attachments.all()]
        return context
