from django.contrib import admin
from .models import MovieRent

# Register your models here.
@admin.register(MovieRent)
class MovieRentAdmin (admin.ModelAdmin):
    list_display = ('id', 'movie', 'customer', 'reserve_date', 'return_date') 
    list_editable = ('return_date',)

    
