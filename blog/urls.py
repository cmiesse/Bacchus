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
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('soiree/', SoireeListView.as_view(), name='soiree-list'),
    path('soiree/<int:pk>/detail', SoireeDetailView.as_view(), name='soiree-detail'),
    path('soiree/new/', SoireeCreateView.as_view(), name='soiree-create'),
    path('soiree/<int:pk>/update/', SoireeUpdateView.as_view(), name='soiree-update'),
    path('vin/', VinListView.as_view(), name='vin-list'),
    path('vin/<int:pk>/', VinDetailView.as_view(), name='vin-detail'),
    path('vin/new/', VinCreateView.as_view(), name='vin-create'),
    path('vin/<int:pk>/update/', VinUpdateView.as_view(), name='vin-update'),
    path('vin/<int:pk>/delete/', VinDeleteView.as_view(), name='vin-delete'),
    path('about/', views.about, name='blog-about'),
]