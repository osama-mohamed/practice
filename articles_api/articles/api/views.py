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


class UpdateArticle(RetrieveUpdateAPIView):
    serializer_class = ArticleSerializer
    queryset = Articles.objects.all()


class NewArticle(APIView):
    # parser_classes = (FileUploadParser, )

    def post(self, request):
        print(request)
        print(request.data)
        img = request.data['file']
        title = request.data['title']
        body = request.data['body']
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
