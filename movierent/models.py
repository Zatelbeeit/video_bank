from django.db import models
from customers.models import MyProfile
from movies.models import MovieGenre, Movie
from django.utils import timezone

from django.utils.translation import ugettext_lazy as _

# Create your models here.
#not sure what this is for - model decider???


class MovieRent(models.Model):
    customer = models.ForeignKey(MyProfile, on_delete=models.CASCADE, related_name="customer")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="rents")
    reserve_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(blank=True, null=True)

    