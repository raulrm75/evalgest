from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'evalgest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^preeval/', include('preeval.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
