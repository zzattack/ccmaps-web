from coffin.conf.urls import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^accounts/', include('registration.backends.simple.urls')),
    
    url(r'^/news', include('ccmaps.news.urls')),
    url(r'^/news', include('ccmaps.tool.urls')),
    url(r'^/maps', include('ccmaps.maps.urls')),
    url(r'^/', include('ccmaps.maps.urls')),
    url(r'^', include('ccmaps.home.urls')),
)
