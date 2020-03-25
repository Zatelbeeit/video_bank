from django.shortcuts import render
from .models import Movie, MovieGenre
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.base import TemplateView
# Create your views here.

class HomePageView(TemplateView):
    template_name="index.html"
    
class MovieListView(ListView):
    model = Movie

    

class MovieDetailView(DetailView):
    model = Movie    

class MovieCreateView(PermissionRequiredMixin, CreateView):
    model = Movie
    fields = "__all__"
    success_url = reverse_lazy('movie-list')

    def get_success_url(self):
        kwargs = MovieCreateView.get_success_url
        return reverse('movie-detail',kwargs={'slug': self.object.slug})

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(MovieCreateView, self).get_form_kwargs(
            *args, **kwargs)
        return kwargs

    permission_required = 'movie.add_movie'

class MovieUpdateView(PermissionRequiredMixin, UpdateView):
    model = Movie
    fields = "__all__"

    def get_success_url(self):
        kwargs = MovieUpdateView.get_success_url
        return reverse('movie-detail',kwargs={'slug': self.object.slug})

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(MovieUpdateView, self).get_form_kwargs(
            *args, **kwargs)
        return kwargs

    permission_required = 'movie.change_movie'

class MovieDeleteView(PermissionRequiredMixin, DeleteView):
    model = Movie
    success_url = reverse_lazy('movie-list')

    permission_required = 'movie.delete_movie'
