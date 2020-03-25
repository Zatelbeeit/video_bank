from .models import VisitStat
from datetime import date
class MiddlewareVisitStats:
    def __init__(self,get_response):
        self.get_response = get_response

        
    def __call__(self,request):

        try:
            VisitStat.objects.create(
                url = request.path,
                IP = request.META.get('REMOTE_ADDR'),
                date = date.today(),
                )
        except:
            pass

    # def count(request):
    #     pageCount = request.url
    #     counter = pageCount.objects.all().count()+1

        return self.get_response(request)
        
        