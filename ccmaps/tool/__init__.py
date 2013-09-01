from django.contrib import admin
from models import *
from admins import *

admin.site.register(ProgramVersion, ProgramVersionAdmin)
