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

		# attachments
		url(r'^attachment/(?P<pk>\d+)/delete/$', views.attachment_delete_view, name='attachment_delete'),
		url(r'^attachment/item/(?P<pk>\d+)/add/$', views.item_attachment_add_view, name='item_attachment_add'),
		url(r'^attachment/crm/(?P<pk>\d+)/add/$', views.crm_attachment_add_view, name='crm_attachment_add'),
		
		# fiscalyears
		url(r'^fiscalyears/$', views.MyFiscalYearList.as_view(), name='fiscalyear_list'),
		url(r'^fiscalyear/add/$', views.MyFiscalYearAdd.as_view(), name='fiscalyear_add'),
		url(r'^fiscalyear/(?P<pk>\d+)/delete/$', views.MyFiscalYearDelete.as_view(), name='fiscalyear_delete'),

		# items
		url(r'^items/$', views.MyItemList.as_view(), name='item_list'),		
		url(r'^item/add/$', views.MyItemAdd.as_view(), name='item_add'),
		url(r'^item/(?P<pk>\d+)/$', views.MyItemDetail.as_view(), name='item_detail'),		
		url(r'^item/(?P<pk>\d+)/edit/$', views.MyItemEdit.as_view(), name='item_edit'),
		url(r'^item/(?P<pk>\d+)/delete/$', views.MyItemDelete.as_view(), name='item_delete'),
		url(r'^item/inv/add/$', views.MyItemInventoryAdd.as_view(), name='item_inv_add'),	

		# crms
		url(r'^vendors/$', views.MyVendorList.as_view(), name='vendor_list'),		
		url(r'^vendor/add/$', views.MyVendorAdd.as_view(), name='vendor_add'),
		url(r'^vendor/(?P<pk>\d+)/edit/$', views.MyVendorEdit.as_view(), name='vendor_edit'),

		url(r'^customers/$', views.MyCustomerList.as_view(), name='customer_list'),	
		url(r'^customer/add/$', views.MyCustomerAdd.as_view(), name='customer_add'),		
		url(r'^customer/(?P<pk>\d+)/edit/$', views.MyCustomerEdit.as_view(), name='customer_edit'),

	)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
