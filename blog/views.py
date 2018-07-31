from django.shortcuts import render, get_object_or_404

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


class ArticleDetailView(DetailView):
    template_name = 'blog/article_detail.html'
    # queryset = Article.objects.all()

    def get_object(self):
        return get_object_or_404(Article, id=self.kwargs.get('id'))