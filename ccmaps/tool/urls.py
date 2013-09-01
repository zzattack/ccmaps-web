from coffin.conf.urls import *
from views import *

urlpatterns = patterns('',
	(r'^$', 'index'),
	(r'^version_check$', version_check),
	(r'^get_latest$', get_latest),
)
