from django.contrib import admin
from .models import Post, Soiree, Vin

class SoireeAdmin(admin.ModelAdmin):
    list_display = (
    'theme',
    'date_soiree'
    )

class PostAdmin(admin.ModelAdmin):
    list_display = (
    'titre',
    'date_post',
    'auteur'
    )

class VinAdmin(admin.ModelAdmin):
    list_display = (
        'pays', 'region', 'appelation', 'cru', 'couleur'
    )



admin.site.register(Post, PostAdmin)
admin.site.register(Soiree, SoireeAdmin)
admin.site.register(Vin, VinAdmin)