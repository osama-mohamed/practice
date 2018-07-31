from django.shortcuts import render

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)


from .models import Article

class ArticleListView(ListView):
    template_name = 'blog/article_list.html'
    queryset = Article.objects.all()