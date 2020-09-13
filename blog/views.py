from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Soiree, Vin


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_post']
    #paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    #paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(auteur=user).order_by('-date_post')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['titre', 'contenu']

    def form_valid(self, form):
        form.instance.auteur = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['titre', 'contenu']

    def form_valid(self, form):
        form.instance.auteur = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.auteur:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.auteur:
            return True
        return False

class SoireeListView(ListView):
    model = Soiree
    template_name = 'blog/soiree.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'soirees'
    ordering = ['-date_soiree']

class SoireeDetailView(DetailView):
    model = Soiree

class SoireeCreateView(LoginRequiredMixin, CreateView):
    model = Soiree
    fields = ['theme', 'date_soiree']

class SoireeUpdateView(LoginRequiredMixin, UpdateView):
    model = Soiree
    fields = ['pays', 'region', 'appelation', 'cru', 'couleur', 'lieu_achat', 'prix_achat', 'millesime', 'cepages', 'proprietaire', 'degre']

class VinListView(ListView):
    model = Vin
    template_name = 'blog/vin.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'vins'

class VinDetailView(DetailView):
    model = Vin

class VinCreateView(LoginRequiredMixin, CreateView):
    model = Vin
    fields = ['pays', 'region', 'appelation', 'cru', 'couleur', 'lieu_achat', 'prix_achat', 'millesime', 'cepages', 'proprietaire', 'degre']

class VinUpdateView(LoginRequiredMixin, UpdateView):
    model = Vin
    fields = ['pays', 'region', 'appelation', 'cru', 'couleur', 'lieu_achat', 'prix_achat', 'millesime', 'cepages', 'proprietaire', 'degre']

class VinDeleteView(LoginRequiredMixin, DeleteView):
    model = Vin
    success_url = 'vin/'

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})