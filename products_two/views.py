from django.views.generic import View, ListView, TemplateView
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.http import HttpResponseRedirect


def redirect_view(request):
  return HttpResponseRedirect('https://github.com/osama-mohamed')
