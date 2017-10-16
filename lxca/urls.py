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
    url(r'^catalog/server/add/$', views.CatalogServerAdd.as_view(),
        name='catalog_server_add'),
    url(r'^catalog/server/(?P<pk>\d+)/delete/$',
        views.CatalogServerDelete.as_view(), name='catalog_server_delete'),
    url(r'^catalog/server/(?P<pk>\d+)/edit/$',
        views.CatalogServerEdit.as_view(), name='catalog_server_edit'),
    url(r'^catalog/server/(?P<pk>\d+)/$',
        views.CatalogServerDetail.as_view(), name='catalog_server_detail'),

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
    url(r'^ref/solution/add/$', views.ArchitectSolutionAdd.as_view(),
        name='sa_solution_add'),
    url(r'^ref/solution/(?P<pk>\d+)/delete/$',
        views.ArchitectSolutionDelete.as_view(), name='sa_solution_delete'),
    url(r'^ref/solution/(?P<pk>\d+)/edit/$',
        views.ArchitectSolutionEdit.as_view(), name='sa_solution_edit'),
    url(r'^ref/solution/(?P<pk>\d+)/$',
        views.ArchitectSolutionDetail.as_view(), name='sa_solution_detail'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
