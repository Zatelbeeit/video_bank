from django.core.management.base import BaseCommand, CommandError
import csv
from movies.models import Movie, MovieGenre
from datetime import datetime
import datetime
import dateparser
import time
class Command(BaseCommand):

    def handle(self, *args, **options):
        Movie.objects.all().delete()
        with open ('./data/netflix_titles.csv') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                nf_id, style, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description = row
                if style == 'Movie':

                    moviegenres = MovieGenre.objects.create(
                        label = listed_in,
                    )
                    moviegenres.save()
                    
                    now = datetime.datetime.now()
                    sec = (now - dateparser.parse(duration)).total_seconds()
                    length = time.strftime('%H:%M:%S', time.gmtime(sec))

                    movies = Movie.objects.create(
                        actors = cast,
                        country = country,
                        director = director,
                        length = length,
                        release_date = datetime.datetime.strptime(release_year, "%Y").strftime('%Y-01-01'),
                        synopsis = description,
                        title = title,
                        trailer_url = 'www.nimporte-quoi.com',
                        
                    )
                    movies.save()
                
                    # print(nf_id, style, title, director, cast, country, date_added, release_date, rating, duration, listed_in, description)
                