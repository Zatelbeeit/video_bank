from django.contrib import admin
from .models import MovieGenre, Movie
from linguist.admin import TranslatableModelAdmin
# Register your models here.


@admin.register(MovieGenre)
class MovieGenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Movie)
class MovieAdmin(TranslatableModelAdmin):
    
    list_display = ["title" , "release_date"]

