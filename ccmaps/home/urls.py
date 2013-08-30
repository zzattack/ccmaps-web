from coffin.conf.urls import *
from ccmaps.home.views import *

urlpatterns = patterns('',
	url(r'^$', index),
	url(r'^contact$',  contact),
)