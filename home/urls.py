from django.urls import *
from home.views import *

urlpatterns = [
	re_path(r'^(?:index.*)?$(?i)', index, name='index'),
	re_path(r'^contact$(?i)', contact, name='contact'),
]