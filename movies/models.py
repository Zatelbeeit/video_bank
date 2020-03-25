from django.db import models
from autoslug import AutoSlugField
from django.utils.timezone import datetime
from six import with_metaclass
from django.utils.translation import ugettext_lazy as _
from linguist.metaclasses import ModelMeta as LinguistMeta
from linguist.mixins import ManagerMixin as LinguistManagerMixin
from linguist.models.base import Translation
# Create your models here.



class MovieGenre(models.Model):
    label = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='label', null=True)
    

    def __str__(self):
            return self.label

    

class MovieTranslation(Translation):
    class Meta:
        abstract = False

class MovieManager(LinguistManagerMixin, models.Manager):
    pass

class Movie(with_metaclass(LinguistMeta,models.Model)):
    actors = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    director = models.CharField(max_length=100, verbose_name =_('director'))
    length = models.TimeField()
    picture = models.ImageField(upload_to='uploads/',
                                height_field=None, 
                                width_field=None, 
                                max_length=100,
                                null = True,
                                blank=True)
    release_date = models.DateField()
    slug = AutoSlugField(populate_from='title', max_length=255, null=True)
    synopsis = models.TextField()
    title = models.CharField(max_length=100)
    trailer_url = models.URLField()
    movie_genres = models.ManyToManyField(MovieGenre)
    objects= MovieManager()

    class Meta:
        verbose_name= _('movie')
        verbose_name_plural = _('movies')
        linguist = {
            'identifier' : 'whatever',
            'fields':('actors', 'country', 'director', 'synopsis', 'title' ),
            'default_language': 'en',
          
            'decider': MovieTranslation,
        }    

    def __str__(self):
        return self.title

    def is_out(self):
        if self.rents.filter(return_date=None).count() != 0:
            return True
        else:
            return False
