from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    SoireeListView,
    SoireeDetailView,
    SoireeCreateView,
    SoireeUpdateView,
    VinListView,
    VinDetailView,
    VinCreateView,
    VinUpdateView,
    VinDeleteView,
    FicheListView,
    UserFicheListView,
    FicheDetailView,
    FicheCreateView,
    FicheUpdateView,
    FicheDeleteView,
    VinFicheListView,
    HomePageView
)
from . import views

urlpatterns = [
    #path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/detail', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('soiree/', SoireeListView.as_view(), name='soiree-list'),
    path('soiree/<int:pk>/detail', SoireeDetailView.as_view(), name='soiree-detail'),
    path('soiree/new/', SoireeCreateView.as_view(), name='soiree-create'),
    path('soiree/<int:pk>/update/', SoireeUpdateView.as_view(), name='soiree-update'),
    path('vin/', VinListView.as_view(), name='vin-list'),
    path('vin/<int:pk>/detail', VinDetailView.as_view(), name='vin-detail'),
    path('vin/new/', VinCreateView.as_view(), name='vin-create'),
    path('vin/<int:pk>/update/', VinUpdateView.as_view(), name='vin-update'),
    path('vin/<int:pk>/delete/', VinDeleteView.as_view(), name='vin-delete'),
    path('fiche/', FicheListView.as_view(),name='fiche-list'),
    path('user/<str:username>/fiche/', UserFicheListView.as_view(), name='user-fiches'),
    path('fiche/<int:pk>/detail', FicheDetailView.as_view(), name='fiche-detail'),
    path('fiche/new/', FicheCreateView.as_view(), name='fiche-create'),
    path('fiche/<int:pk>/update/', FicheUpdateView.as_view(), name='fiche-update'),
    path('fiche/<int:pk>/delete/', FicheDeleteView.as_view(), name='fiche-delete'),
    path('vin/<int:id>/fiche/', VinFicheListView.as_view(), name='vin-fiches'),
    path('', HomePageView.as_view(), name='blog-about'),
]