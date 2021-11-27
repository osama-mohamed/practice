from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect

from .models import Article
from .forms import ArticleForm

# Create your views here.
def article_search_view(request):
  query = request.GET.get('q')
  qs = Article.objects.all()
  if query is not None:
    qs = Article.objects.filter(
      Q(title__icontains=query) |
      Q(content__icontains=query)
    )
  context = {
    'object_list': qs,
  }
  return render(request, 'articles/search.html', context=context)

@login_required
def article_create_view(request):
  form = ArticleForm(request.POST or None)
  context = {
    'form': form
  }
  if form.is_valid():
    article_object = form.save()
    context['form'] = ArticleForm()
    # context['object'] = article_object
    # context['created'] = True
    # return redirect('article-detail', slug=article_object.slug)
    return redirect(article_object.get_absolute_url())
  return render(request, 'articles/create.html', context = context)


def article_detail_view(request, slug=None):
  article_obj = None
  if slug is not None:
    try:
      article_obj = Article.objects.get(slug=slug)
    except Article.DoesNotExist:
      raise Http404
    except Article.MultipleObjectsReturned:
      article_obj = Article.objects.filter(slug=slug).first()
    except:
      raise Http404
  context = {
    'object': article_obj
  }
  return render(request, 'articles/article_detail_view.html', context = context)