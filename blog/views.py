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
from .forms import ArticleModelForm


class ArticleListView(ListView):
    template_name = 'blog/article_list.html'
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    template_name = 'blog/article_detail.html'
    # queryset = Article.objects.all()

    def get_object(self):
        return get_object_or_404(Article, id=self.kwargs.get('id'))


class ArticleCreateView(CreateView):
    form_class = ArticleModelForm
    template_name = 'blog/article_create.html'
    queryset = Article.objects.all()
    # success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)
    
    # def get_success_url(self):
    #     return '/'


class ArticleUpdateView(UpdateView):
    form_class = ArticleModelForm
    template_name = 'blog/article_create.html'
    # queryset = Article.objects.all()
    # success_url = '/'

    def get_object(self):
        return get_object_or_404(Article, id=self.kwargs.get('id'))

    def form_valid(self, form):
        return super().form_valid(form)
    
    # def get_success_url(self):
    #     return '/'