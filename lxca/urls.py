import django.contrib.auth.views as AuthViews
from django.conf import settings
from django.conf.urls import patterns
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.edit import CreateView

from lxca import views

urlpatterns = patterns(
    '',
    # url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^$',
        views.LoginView.as_view(),
        name='home'),
    url(r'login/$',
        views.LoginView.as_view(),
        name='login'),
    url(r'logout/$',
        views.LogoutView.as_view(),
        name='logout'),
    url(r'^register/$',
        views.UserRegisterView.as_view(),
        name='user_register'),

    # catalog racks
    url(r'^attachment/catalog/rack/(?P<pk>\d+)/add/$',
        views.CatalogRack_attachment_add,
        name='catalog_rack_attachment_add'),
    url(r'^attachment/catalog/rack/(?P<pk>\d+)/delete/$',
        views.CatalogRack_attachment_delete,
        name='catalog_rack_attachment_delete'),
    url('^catalog/racks/$',
        views.CatalogRackList.as_view(),
        name='catalog_rack_list'),
    url(r'^catalog/rack/add/$',
        views.CatalogRackAdd.as_view(),
        name='catalog_rack_add'),
    url(r'^catalog/rack/(?P<pk>\d+)/delete/$',
        views.CatalogRackDelete.as_view(),
        name='catalog_rack_delete'),
    url(r'^catalog/rack/(?P<pk>\d+)/edit/$',
        views.CatalogRackEdit.as_view(),
        name='catalog_rack_edit'),
    url(r'^catalog/rack/(?P<pk>\d+)/$',
        views.CatalogRackDetail.as_view(),
        name='catalog_rack_detail'),

    # catalog switches
    url(r'^attachment/catalog/switch/(?P<pk>\d+)/add/$',
        views.CatalogSwitch_attachment_add,
        name='catalog_switch_attachment_add'),
    url(r'^attachment/catalog/switch/(?P<pk>\d+)/delete/$',
        views.CatalogSwitch_attachment_delete,
        name='catalog_switch_attachment_delete'),
    url('^catalog/switches/$',
        views.CatalogSwitchList.as_view(),
        name='catalog_switch_list'),
    url(r'^catalog/switch/add/$',
        views.CatalogSwitchAdd.as_view(),
        name='catalog_switch_add'),
    url(r'^catalog/switch/(?P<pk>\d+)/delete/$',
        views.CatalogSwitchDelete.as_view(),
        name='catalog_switch_delete'),
    url(r'^catalog/switch/(?P<pk>\d+)/edit/$',
        views.CatalogSwitchEdit.as_view(),
        name='catalog_switch_edit'),
    url(r'^catalog/switch/(?P<pk>\d+)/$',
        views.CatalogSwitchDetail.as_view(),
        name='catalog_switch_detail'),

    # catalog servers
    url(r'^attachment/catalog/server/(?P<pk>\d+)/add/$',
        views.CatalogServer_attachment_add,
        name='catalog_server_attachment_add'),
    url(r'^attachment/catalog/server/(?P<pk>\d+)/delete/$',
        views.CatalogServer_attachment_delete,
        name='catalog_server_attachment_delete'),
    url('^catalog/servers/$',
        views.CatalogServerList.as_view(),
        name='catalog_server_list'),
    url(r'^catalog/server/add/$',
        views.CatalogServerAdd.as_view(),
        name='catalog_server_add'),
    url(r'^catalog/server/(?P<pk>\d+)/delete/$',
        views.CatalogServerDelete.as_view(),
        name='catalog_server_delete'),
    url(r'^catalog/server/(?P<pk>\d+)/edit/$',
        views.CatalogServerEdit.as_view(),
        name='catalog_server_edit'),
    url(r'^catalog/server/(?P<pk>\d+)/$',
        views.CatalogServerDetail.as_view(),
        name='catalog_server_detail'),

    # architect solution
    url(r'^attachment/ref/solution/(?P<pk>\d+)/add/$',
        views.ArchitectSolution_attachment_add,
        name='sa_solution_attachment_add'),
    url(r'^attachment/ref/solution/(?P<pk>\d+)/delete/$',
        views.ArchitectSolution_attachment_delete,
        name='sa_solution_attachment_delete'),

    url('^ref/solutions/$',
        views.ArchitectSolutionList.as_view(),
        name='sa_solution_list'),
    url(r'^ref/solution/add/$',
        views.ArchitectSolutionAdd.as_view(),
        name='sa_solution_add'),
    url(r'^ref/solution/(?P<pk>\d+)/delete/$',
        views.ArchitectSolutionDelete.as_view(),
        name='sa_solution_delete'),
    url(r'^ref/solution/(?P<pk>\d+)/edit/$',
        views.ArchitectSolutionEdit.as_view(),
        name='sa_solution_edit'),
    url(r'^ref/solution/(?P<pk>\d+)/$',
        views.ArchitectSolutionDetail.as_view(),
        name='sa_solution_detail'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
