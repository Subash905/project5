from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def soumya(request):
    return HttpResponse('<marquee><h1>This is app2 first view</h1></marquee>')
def subash(request):
    return HttpResponse('<marquee><h1>This is app2 Second View</h1></marquee>')
        
