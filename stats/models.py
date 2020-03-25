from django.db import models
from django.utils.timezone import datetime

# Create your models here.
class VisitStat(models.Model):
    url = models.URLField()
    counter = models.IntegerField(default=0)
    IP = models.GenericIPAddressField()
    date = models.DateField()

    class Meta:
        unique_together = ('url', 'IP', 'date')