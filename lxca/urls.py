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
from lxca import catalog_views as catalog
from lxca import architect_views as architect
from lxca import order_views as order

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
        catalog.CatalogRack_attachment_add,
        name='catalog_rack_attachment_add'),
    url(r'^attachment/catalog/rack/(?P<pk>\d+)/delete/$',
        catalog.CatalogRack_attachment_delete,
        name='catalog_rack_attachment_delete'),
    url('^catalog/racks/$',
        catalog.CatalogRackList.as_view(),
        name='catalog_rack_list'),
    url(r'^catalog/rack/add/$',
        catalog.CatalogRackAdd.as_view(),
        name='catalog_rack_add'),
    url(r'^catalog/rack/(?P<pk>\d+)/delete/$',
        catalog.CatalogRackDelete.as_view(),
        name='catalog_rack_delete'),
    url(r'^catalog/rack/(?P<pk>\d+)/edit/$',
        catalog.CatalogRackEdit.as_view(),
        name='catalog_rack_edit'),
    url(r'^catalog/rack/(?P<pk>\d+)/$',
        catalog.CatalogRackDetail.as_view(),
        name='catalog_rack_detail'),

    # catalog switches
    url(r'^attachment/catalog/switch/(?P<pk>\d+)/add/$',
        catalog.CatalogSwitch_attachment_add,
        name='catalog_switch_attachment_add'),
    url(r'^attachment/catalog/switch/(?P<pk>\d+)/delete/$',
        catalog.CatalogSwitch_attachment_delete,
        name='catalog_switch_attachment_delete'),
    url('^catalog/switches/$',
        catalog.CatalogSwitchList.as_view(),
        name='catalog_switch_list'),
    url(r'^catalog/switch/add/$',
        catalog.CatalogSwitchAdd.as_view(),
        name='catalog_switch_add'),
    url(r'^catalog/switch/(?P<pk>\d+)/delete/$',
        catalog.CatalogSwitchDelete.as_view(),
        name='catalog_switch_delete'),
    url(r'^catalog/switch/(?P<pk>\d+)/edit/$',
        catalog.CatalogSwitchEdit.as_view(),
        name='catalog_switch_edit'),
    url(r'^catalog/switch/(?P<pk>\d+)/$',
        catalog.CatalogSwitchDetail.as_view(),
        name='catalog_switch_detail'),

    # catalog PDUs
    url(r'^attachment/catalog/pdu/(?P<pk>\d+)/add/$',
        catalog.CatalogPdu_attachment_add,
        name='catalog_pdu_attachment_add'),
    url(r'^attachment/catalog/pdu/(?P<pk>\d+)/delete/$',
        catalog.CatalogPdu_attachment_delete,
        name='catalog_pdu_attachment_delete'),
    url('^catalog/pdues/$',
        catalog.CatalogPduList.as_view(),
        name='catalog_pdu_list'),
    url(r'^catalog/pdu/add/$',
        catalog.CatalogPduAdd.as_view(),
        name='catalog_pdu_add'),
    url(r'^catalog/pdu/(?P<pk>\d+)/delete/$',
        catalog.CatalogPduDelete.as_view(),
        name='catalog_pdu_delete'),
    url(r'^catalog/pdu/(?P<pk>\d+)/edit/$',
        catalog.CatalogPduEdit.as_view(),
        name='catalog_pdu_edit'),
    url(r'^catalog/pdu/(?P<pk>\d+)/$',
        catalog.CatalogPduDetail.as_view(),
        name='catalog_pdu_detail'),

    # catalog servers
    url(r'^attachment/catalog/server/(?P<pk>\d+)/add/$',
        catalog.CatalogServer_attachment_add,
        name='catalog_server_attachment_add'),
    url(r'^attachment/catalog/server/(?P<pk>\d+)/delete/$',
        catalog.CatalogServer_attachment_delete,
        name='catalog_server_attachment_delete'),
    url('^catalog/servers/$',
        catalog.CatalogServerList.as_view(),
        name='catalog_server_list'),
    url(r'^catalog/server/add/$',
        catalog.CatalogServerAdd.as_view(),
        name='catalog_server_add'),
    url(r'^catalog/server/(?P<pk>\d+)/delete/$',
        catalog.CatalogServerDelete.as_view(),
        name='catalog_server_delete'),
    url(r'^catalog/server/(?P<pk>\d+)/edit/$',
        catalog.CatalogServerEdit.as_view(),
        name='catalog_server_edit'),
    url(r'^catalog/server/(?P<pk>\d+)/$',
        catalog.CatalogServerDetail.as_view(),
        name='catalog_server_detail'),

    # playbook
    url('^ref/playbooks/$',
        architect.PlaybookList.as_view(),
        name='sa_playbook_list'),
    url(r'^ref/playbook/add/$',
        architect.PlaybookAdd.as_view(),
        name='sa_playbook_add'),
    url(r'^ref/playbook/(?P<pk>\d+)/delete/$',
        architect.PlaybookDelete.as_view(),
        name='sa_playbook_delete'),
    url(r'^ref/playbook/(?P<pk>\d+)/edit/$',
        architect.PlaybookEdit.as_view(),
        name='sa_playbook_edit'),

    # architect application
    url(r'^attachment/ref/application/(?P<pk>\d+)/add/$',
        architect.ArchitectApplication_attachment_add,
        name='sa_application_attachment_add'),
    url(r'^attachment/ref/application/(?P<pk>\d+)/delete/$',
        architect.ArchitectApplication_attachment_delete,
        name='sa_application_attachment_delete'),
    url('^ref/applications/$',
        architect.ArchitectApplicationList.as_view(),
        name='sa_application_list'),
    url(r'^ref/application/add/$',
        architect.ArchitectApplicationAdd.as_view(),
        name='sa_application_add'),
    url(r'^ref/application/(?P<pk>\d+)/delete/$',
        architect.ArchitectApplicationDelete.as_view(),
        name='sa_application_delete'),
    url(r'^ref/application/(?P<pk>\d+)/edit/$',
        architect.ArchitectApplicationEdit.as_view(),
        name='sa_application_edit'),
    url(r'^ref/application/(?P<pk>\d+)/$',
        architect.ArchitectApplicationDetail.as_view(),
        name='sa_application_detail'),

    # architect solution
    url(r'^attachment/ref/solution/(?P<pk>\d+)/add/$',
        architect.ArchitectSolution_attachment_add,
        name='sa_solution_attachment_add'),
    url(r'^attachment/ref/solution/(?P<pk>\d+)/delete/$',
        architect.ArchitectSolution_attachment_delete,
        name='sa_solution_attachment_delete'),
    url('^ref/solutions/$',
        architect.ArchitectSolutionList.as_view(),
        name='sa_solution_list'),
    url(r'^ref/solution/add/$',
        architect.ArchitectSolutionAdd.as_view(),
        name='sa_solution_add'),
    url(r'^ref/solution/(?P<pk>\d+)/delete/$',
        architect.ArchitectSolutionDelete.as_view(),
        name='sa_solution_delete'),
    url(r'^ref/solution/(?P<pk>\d+)/edit/$',
        architect.ArchitectSolutionEdit.as_view(),
        name='sa_solution_edit'),
    url(r'^ref/solution/(?P<pk>\d+)/$',
        architect.ArchitectSolutionDetail.as_view(),
        name='sa_solution_detail'),

    # order solution
    url('^order/solutions/$',
        order.OrderSolutionList.as_view(),
        name='order_solution_list'),
    url(r'^order/solution/add/$',
        order.OrderSolutionAdd.as_view(),
        name='order_solution_add'),
    url(r'^order/solution/(?P<pk>\d+)/delete/$',
        order.OrderSolutionDelete.as_view(),
        name='order_solution_delete'),
    url(r'^order/solution/(?P<pk>\d+)/edit/$',
        order.OrderSolutionEdit.as_view(),
        name='order_solution_edit'),
    url(r'^order/solution/(?P<pk>\d+)/$',
        order.OrderSolutionDetail.as_view(),
        name='order_solution_detail'),

    # order pdu
    url('^order/pdus/$',
        order.OrderPduList.as_view(),
        name='order_pdu_list'),
    url(r'^order/pdu/(?P<pk>\d+)/edit/$',
        order.OrderPduEdit.as_view(),
        name='order_pdu_edit'),

    # order switch
    url('^order/switches/$',
        order.OrderSwitchList.as_view(),
        name='order_switch_list'),
    url(r'^order/switch/(?P<pk>\d+)/edit/$',
        order.OrderSwitchEdit.as_view(),
        name='order_switch_edit'),

    # order server
    url('^order/servers/$',
        order.OrderServerList.as_view(),
        name='order_server_list'),
    url(r'^order/server/(?P<pk>\d+)/edit/$',
        order.OrderServerEdit.as_view(),
        name='order_server_edit'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
