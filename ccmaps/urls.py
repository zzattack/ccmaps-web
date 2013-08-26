from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from ccmaps import home, news, discussions

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^maps/', include('ccmaps.maps.urls')),
    url(r'^news/', include('ccmaps.news.urls')),
    url(r'^discuss/', include('ccmaps.discussions.urls')),

    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^profiles/', include('profiles.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'', include('ccmaps.home.urls')),
)
