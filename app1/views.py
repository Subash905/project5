from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('<h1>This is app1 first view</h2>')
def second(request):
    return HttpResponse('<h2>This is app1 second view</h2>')