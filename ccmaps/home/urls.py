from django.conf.urls import *
from .views import *

urlpatterns = patterns('',
	url(r'^$', index),
	url(r'^contact$',  contact),
)