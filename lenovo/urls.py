from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from django.contrib import admin
# tastypie API urls
from tastypie.api import Api

import settings
from lxca.api import *

v1_api = Api(api_name='v1')
v1_api.register(CatalogServerResource())
v1_api.register(ArchitectSolutionResource())

urlpatterns = patterns(
    '',
    url(r'^api/',
        include(v1_api.urls)),
    url(r'^admin/',
        include(admin.site.urls)),
    url('', include('django.contrib.auth.urls',
                    namespace='auth')),
    url(r'^lxca/',
        include('lxca.urls')),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )

    urlpatterns += patterns(
        'django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )
