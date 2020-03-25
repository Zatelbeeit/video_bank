from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import MovieRent
from movies.models import Movie
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.utils.timezone import datetime
# Create your views here.
class MovieRentView(DetailView):
    model = Movie

    def get(self, request, *args, **kwargs):
        film = self.get_object()
        customer = request.user.my_profile
        
        MovieRent.objects.create(
            movie = film,
            customer = customer
        )

        return HttpResponseRedirect(reverse('movie-list')) 

class MovieRentListView(ListView):
    model = MovieRent

    def get(self, request, *args, **kwargs):
        film = self.get_object()
        customer = request.user.my_profile
        
        MovieRent.objects.create(
            movie = film,
            customer = customer
        )

        return HttpResponseRedirect(reverse('movie-list'))
        
   
   