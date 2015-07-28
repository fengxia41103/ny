from django.conf.urls import patterns, url
from django.conf.urls import url
from intern import views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
import django.contrib.auth.views as AuthViews
from django.views.decorators.csrf import ensure_csrf_cookie
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page

urlpatterns = patterns(
		'',
		# url(r'^$', views.HomeView.as_view(), name='home'),
		url(r'^$', views.LoginView.as_view(), name='home'),
		url(r'login/$', views.LoginView.as_view(),name='login'),
		url(r'logout/$', views.LogoutView.as_view(), name='logout'),
		url(r'^register/$', views.UserRegisterView.as_view(), name='user_register'),

		url(r'^application/$', views.MyApplicationList.as_view(), name='application_list'),
		url(r'^application/add/$', views.MyApplicationAdd.as_view(), name='application_add'),
		url(r'^application/update/$', views.MyApplicationAdd.as_view(), name='application_add'),
		url(r'^application/(?P<pk>\d+)/edit/$', views.MyApplicationEdit.as_view(), name='application_edit'),
		url(r'^application/(?P<pk>\d+)/delete/$', views.MyApplicationDelete.as_view(), name='application_delete'),
		url(r'^application/(?P<pk>\d+)/$', views.MyApplicationDetail.as_view(), name='application_detail'),		
		url(r'^application/status/update/$', views.MyApplicationStatusUpdate.as_view(), name='application_status_update'),
		url(r'^application/(?P<pk>\d+)/reminder/$', views.MyApplicationReminder.as_view(), name='application_reminder'),

		url(r'^status/audit/(?P<pk>\d+)/delete/$', views.MyStatusAuditDelete.as_view(), name='status_audit_delete'),

		# moving 
		url(r'^items/$', views.MyItemList.as_view(), name='item_list'),
		url(r'^item/(?P<pk>\d+)/edit/$', views.MyItemEdit.as_view(), name='item_edit'),
		url(r'^item/(?P<pk>\d+)/delete/$', views.MyItemDelete.as_view(), name='item_delete'),

		url(r'^boxes/$', views.MyBoxList.as_view(), name='box_list'),
		url(r'^boxes/status/(\w+)/$', views.MyBoxListByStatus.as_view(), name='box_list_by_status'),
		url(r'^boxes/size/(\w+)/$', views.MyBoxListBySize.as_view(), name='box_list_by_size'),
		
		url(r'^box/(?P<pk>\d+)/edit/$', views.MyBoxEdit.as_view(), name='box_edit'),
		url(r'^box/update/$', views.MyBoxUpdate.as_view(), name='box_update'),
		url(r'^box/(?P<pk>\d+)/delete/$', views.MyBoxDelete.as_view(), name='box_delete'),

	)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
