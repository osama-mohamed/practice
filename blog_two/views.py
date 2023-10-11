from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def redirect_somewhere(request):
  return HttpResponse(f'{request.path} | {request.method}')