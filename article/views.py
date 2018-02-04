from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View

from .models import Article, Category


class AllArticlesListView(ListView):
    template_name = 'article/all_articles.html'
    queryset = Article.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(AllArticlesListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ArticleDetailView(DetailView):
    template_name = 'article/article_detail.html'

    def get_object(self):
        slug = self.kwargs['slug']
        article = Article.objects.filter(slug=slug).first()
        article.number_of_views += 1
        article.save()
        return get_object_or_404(Article, slug=slug, publish=True)


class ArticlesByCategoryListView(ListView):
    template_name = 'article/all_articles.html'
    queryset = ''

    def get_context_data(self, **kwargs):
        context = super(ArticlesByCategoryListView, self).get_context_data(**kwargs)
        context['object_list'] = Article.objects.filter(category__category=self.kwargs['category']).order_by('-id')
        context['categories'] = Category.objects.all()
        return context
