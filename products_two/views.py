from django.views.generic import View, ListView, TemplateView
from django.views.decorators.http import require_http_methods
from django.shortcuts import render


def about_us_view(request):
  return render(request, 'about.html', {})


class AboutUsView(TemplateView):
  template_name = 'about.html'


class AboutUsView(View):
  def get(self, request):
    return render(request, 'about.html', {})