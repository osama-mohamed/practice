from django.shortcuts import render
from articles.models import Article

from random import randint

def home_view(request):
  article_queryset = Article.objects.all()
  article_obj = Article.objects.get(id = randint(5, article_queryset.last().id))
  context = {
    'object': article_obj,
    'object_list': article_queryset,
  }
  return render(request, 'home_view.html', context = context)


def handle404(request, exception):
  return render(request, '404.html', status=404)

def handle500(request):
  return render(request, '500.html', status=500)