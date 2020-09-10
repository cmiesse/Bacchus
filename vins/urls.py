from django.urls import path
from . import views


urlpatterns = [
    path('', views.vins_all),
    path('<int:vin_id>/details', views.detailVin, name="vinDetail")
]