from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    return HttpResponse('<h1>home page</h1>')


def about_view(request, *args, **kwargs):
    return HttpResponse('<h1>about page</h1>')


def contact_view(request, *args, **kwargs):
    return HttpResponse('<h1>contact page</h1>')
