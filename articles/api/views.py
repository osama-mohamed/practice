from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView

from .serializer import ArticleSerializer
from articles.models import Articles


class AllArticles(ListAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer


class NewArticle(CreateAPIView):
    serializer_class = ArticleSerializer
    queryset = ''


class UpdateArticle(RetrieveUpdateAPIView):
    serializer_class = ArticleSerializer
    queryset = Articles.objects.all()
