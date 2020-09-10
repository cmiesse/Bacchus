from django.contrib import admin
from .models import Vin


class VinAdmin(admin.ModelAdmin):
    list_display = (
    'appelation',
    'cru',
    'millesime',
    'degre'
    )


admin.site.register(Vin, VinAdmin)