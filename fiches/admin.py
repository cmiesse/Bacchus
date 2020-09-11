from django.contrib import admin
from .models import Fiche


class FicheAdmin(admin.ModelAdmin):
    list_display = ('limpidite', 'intensite_couleurs')


admin.site.register(Fiche, FicheAdmin)