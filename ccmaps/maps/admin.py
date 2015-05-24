from django.contrib import admin
from .models import *

@admin.register(Map)
class MapAdmin(admin.ModelAdmin): pass

@admin.register(MapProperties)
class MapPropertiesAdmin(admin.ModelAdmin): pass

@admin.register(MapRevision)
class MapRevisionAdmin(admin.ModelAdmin): pass