from django.views import View
from django.http import HttpResponse


class HomePageView(View):
    #Get request
    def get(self,request):
        return HttpResponse('Welcome to Entity HomePage!')

