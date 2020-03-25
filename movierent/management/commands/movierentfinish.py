from django.core.management.base import BaseCommand, CommandError
from movierent.models import MovieRent 
from datetime import date, timedelta
from django.http import HttpResponse
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from django.core.mail import send_mail


class Command(BaseCommand):

    def handle(self, *args, **options):
        for rent in MovieRent.objects.filter(return_date=None):
            reserve_date= rent.reserve_date
            current_date= date.today()
            timediff = current_date - reserve_date
            if timediff > timedelta(days = 14):
                print(rent.customer.user.username)
               
                ctx = {
                    'rent' : rent,
                    'username' : rent.customer.user.username,
                    'site' : 'www.tdc.com',
                    'movie' : rent.movie.title,
                    
                }
                message = render_to_string('movierent/mail/email_reminder.html', ctx)
    
                print(message)