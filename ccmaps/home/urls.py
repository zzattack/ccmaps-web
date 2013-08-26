from django.conf.urls.defaults import patterns, include, url
from ccmaps.home.views import *

urlpatterns = patterns('',
	url(r'^$', index),
	url(r'^contact$',  contact),
)