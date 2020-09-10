from django.contrib import admin
from .models import Soiree


class SoireeAdmin(admin.ModelAdmin):
    list_display = ('nom','date')



admin.site.register(Soiree, SoireeAdmin)