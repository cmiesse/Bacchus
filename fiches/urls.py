from django.urls import path
from . import views


urlpatterns = [
    path('', views.fiches_all),
    path('<int:fiche_id>/details', views.detailFiche, name="ficheDetail"),
]