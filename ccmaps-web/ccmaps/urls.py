from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^/upload/', include('ccmaps.map_uploader')),
    url(r'^/news/', include('ccmaps.news')),
    url(r'^/discuss/', include('ccmaps.discussions')),
    url(r'^/accounts/', include('ccmaps.accounts')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('ccmaps.home')),
)
