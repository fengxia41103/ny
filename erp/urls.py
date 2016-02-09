from django.conf.urls import patterns, url
from django.conf.urls import url
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
import django.contrib.auth.views as AuthViews
from django.views.decorators.csrf import ensure_csrf_cookie
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page
from erp import views

urlpatterns = patterns(
		'',
		# url(r'^$', views.HomeView.as_view(), name='home'),
		url(r'^$', views.LoginView.as_view(), name='home'),
		url(r'login/$', views.LoginView.as_view(),name='login'),
		url(r'logout/$', views.LogoutView.as_view(), name='logout'),
		url(r'^register/$', views.UserRegisterView.as_view(), name='user_register'),

		url(r'^fiscalyears/$', views.MyFiscalYearList.as_view(), name='fiscalyear_list'),
		url(r'^fiscalyear/add/$', views.MyFiscalYearAdd.as_view(), name='fiscalyear_add'),
		url(r'^fiscalyear/(?P<pk>\d+)/delete/$', views.MyFiscalYearDelete.as_view(), name='fiscalyear_delete'),

		url(r'^items/$', views.MyItemList.as_view(), name='item_list'),
		url(r'^item/add/$', views.MyItemAdd.as_view(), name='item_add'),
		url(r'^item/(?P<pk>\d+)/edit/$', views.MyItemEdit.as_view(), name='item_edit'),
		url(r'^item/(?P<pk>\d+)/delete/$', views.MyItemDelete.as_view(), name='item_delete'),
	)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
