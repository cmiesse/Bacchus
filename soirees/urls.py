from django.urls import path
from . import views

# /products
# /products/1/detail
# /products/new

urlpatterns = [
    path('', views.index),
    path('<int:soiree_id>/details', views.detailSoiree, name="soireeDetail")
]
