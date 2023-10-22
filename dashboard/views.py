from multiprocessing import context
from typing import Any
from django import http
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateResponseMixin, ContextMixin
from django.views.generic import TemplateView, View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

class AboutTemplateView(TemplateView):
  template_name = 'dashboard/about.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'About'
    return context
  
class MyView(ContextMixin, TemplateResponseMixin, View):
  template_name = 'dashboard/about.html'

  @method_decorator(login_required)
  def get(self, request, *args, **kwargs):
    context = self.get_context_data(**kwargs)
    return self.render_to_response(context)
  
