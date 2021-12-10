from django.shortcuts import render
from articles.models import Article

from random import randint

def home_view(request):
  article_queryset = Article.objects.all()

  # first_id = article_queryset.first().id
  # last_id = article_queryset.last().id
  # range_numbers = list(range(first_id, last_id+1))
  # ids = list(article_queryset.values_list('id', flat=True).order_by('id'))
  # list_deff_numbers = list(set(range_numbers) - set(ids)) 
  # random_id = randint(first_id, last_id)
  # if random_id in list_deff_numbers:
  #   random_id = randint(first_id, last_id)

  ids = list(article_queryset.values_list('id', flat=True).order_by('id'))
  random_id = randint(ids[0], ids[-1])
  if random_id not in ids:
    random_id = randint(ids[0], ids[-1])

  article_obj = Article.objects.get(id=random_id)
  context = {
    'object': article_obj,
    'object_list': article_queryset,
  }
  return render(request, 'home_view.html', context = context)


def handle404(request, exception):
  return render(request, '404.html', status=404)

def handle500(request):
  return render(request, '500.html', status=500)