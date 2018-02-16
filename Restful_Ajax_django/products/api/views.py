from rest_framework.generics import (
    RetrieveAPIView,
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
)
from rest_framework.views import APIView

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.http import response, HttpResponse, JsonResponse
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED
import json

from .serializers import (
    ProductsSerializer,
    ProductDetailSerializer,
    ProductSerializer,
)
from products.models import Product


class AddProductAPIView(CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny, ]


class UpdateProductsAPIView(RetrieveUpdateAPIView):
    serializer_class = ProductSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    permission_classes = [AllowAny, ]

    def get_queryset(self, *args, **kwargs):
        queryset = Product.objects.filter(id=self.kwargs['id'])
        return queryset


class DeleteProductsAPIView(DestroyAPIView):
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    permission_classes = [AllowAny, ]

    def get_queryset(self, *args, **kwargs):
        queryset = Product.objects.filter(id=self.kwargs['id'])
        return queryset


class AllProductsAPIView(ListAPIView):
    serializer_class = ProductsSerializer
    permission_classes = [AllowAny, ]

    def get_queryset(self, *args, **kwargs):
        queryset = Product.objects.all().order_by('-id')
        return queryset


class ProductDetailAPIView(RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    lookup_field = 'slug'
    permission_classes = [AllowAny, ]

    def get_queryset(self, *args, **kwargs):
        queryset = Product.objects.filter(slug__iexact=self.kwargs['slug'])
        return queryset


class CategoryAPIView(ListAPIView):
    serializer_class = ProductsSerializer
    permission_classes = [AllowAny, ]

    def get_queryset(self, *args, **kwargs):
        queryset = Product.objects.filter(category=self.kwargs['category']).order_by('-id')
        return queryset
