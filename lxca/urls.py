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

    # attachments
    url(r'^attachment/(?P<pk>\d+)/delete/$',
        views.attachment_delete_view,
        name='attachment_delete'),
    url(r'^attachment/server/(?P<pk>\d+)/add/$',
        views.server_attachment_add_view,
        name='server_attachment_add'),

    # servers
    url('^catalog/servers/$',
        views.CatalogServerList.as_view(),
        name='catalog_server_list'),
    url(r'^catalog/server/add/$', views.CatalogServerAdd.as_view(),
        name='catalog_server_add'),
    url(r'^catalog/server/(?P<pk>\d+)/edit/$',
        views.CatalogServerEdit.as_view(), name='catalog_server_edit'),
    url(r'^catalog/server/(?P<pk>\d+)/$',
        views.CatalogServerDetail.as_view(), name='catalog_server_detail'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
