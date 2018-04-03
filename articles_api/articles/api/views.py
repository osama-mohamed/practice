from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView

from .serializer import ArticleSerializer
from articles.models import Articles
from .pagination import ArticlesPageNumberPagination


class AllArticles(ListAPIView):
    queryset = Articles.objects.all().order_by('-pk')
    serializer_class = ArticleSerializer
    pagination_class = ArticlesPageNumberPagination


class NewArticle(CreateAPIView):
    serializer_class = ArticleSerializer
    queryset = ''


class UpdateArticle(RetrieveUpdateAPIView):
    serializer_class = ArticleSerializer
    queryset = Articles.objects.all()


class DeleteArticle(DestroyAPIView):
    serializer_class = ArticleSerializer
    queryset = Articles.objects.all()
