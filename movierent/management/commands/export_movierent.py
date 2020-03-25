from django.core.management.base import BaseCommand, CommandError
import csv
from movierent.models import MovieRent
class Command(BaseCommand):

    def handle(self, *args, **options):
        with open ('./data/movierent.csv','w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            
            writer.writerow(['customer','movie','reserve_date', 'return_date'])
            
            for row in MovieRent.objects.all():
                if row.return_date == None:
                    writer.writerow([row.customer, row.movie.title, row.reserve_date, row.return_date])