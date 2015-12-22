from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.views.generic import ListView
from gd.views import mys

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'globaldjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('gd.urls')),
    url(r'^results', mys),
    url(r'^admin/', include(admin.site.urls)),
)
