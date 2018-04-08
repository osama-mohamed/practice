from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializer import ArticleSerializer
from articles.models import Articles
from .pagination import ArticlesPageNumberPagination

from django.conf import settings
import base64
import importlib
import os
from werkzeug.utils import secure_filename


from rest_framework.parsers import (
    FileUploadParser, FormParser, JSONParser, MultiPartParser
)


class AllArticles(ListAPIView):
    queryset = Articles.objects.all().order_by('-pk')
    serializer_class = ArticleSerializer
    pagination_class = ArticlesPageNumberPagination


# class NewArticle(CreateAPIView):
#     serializer_class = ArticleSerializer
#     queryset = ''


# class UpdateArticle(RetrieveUpdateAPIView):
#     serializer_class = ArticleSerializer
#     queryset = Articles.objects.all()


class UpdateArticle(APIView):

    def put(self, request, pk):
        qs = Articles.objects.filter(pk=pk).first()
        qs.title = request.data['title']
        qs.body = request.data['body']
        qs.img = request.data['file']
        qs.save()
        return Response(status=204)


class NewArticle(APIView):

    def post(self, request):
        title = request.data['title']
        body = request.data['body']
        img = request.data['file']
        article = Articles(
          title=title,
          body=body,
          img=img,
        )
        article.save()
        return Response(status=204)


class DeleteArticle(DestroyAPIView):
    serializer_class = ArticleSerializer
    queryset = Articles.objects.all()
