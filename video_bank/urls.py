"""video_bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from userena import settings as userena_settings
from userena import views as userena_views
from movies.views import HomePageView, MovieListView, MovieDetailView, MovieCreateView, MovieUpdateView, MovieDeleteView
from movierent.views import MovieRentView, MovieRentListView
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n'), name='set_language'),

]


urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('',HomePageView.as_view(), name = 'home'),
    path('customers/', include ('userena.urls')),
    path('movies/',MovieListView.as_view(), name = 'movie-list'),
    path('movie/<slug:slug>',MovieDetailView.as_view(), name='movie-detail'),
    path('movie/add', MovieCreateView.as_view(), name='movie-create'),
    path('movie/<slug:slug>/update', MovieUpdateView.as_view(), name='movie-update'),
    path('movie/<slug:slug>/delete', MovieDeleteView.as_view(), name = 'movie-delete'),
    path('movie/<slug:pk>/reserve/', MovieRentView.as_view(), name='movie-rented'),
    path('movies/out', MovieRentListView.as_view(), name='movie-rented-list'),
)
