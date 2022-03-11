from django.http import Http404
from rest_framework.generics import (
  ListAPIView,
  RetrieveAPIView,
  ListCreateAPIView,
  UpdateAPIView,
  DestroyAPIView,
  GenericAPIView,
)
from rest_framework.mixins import (
  ListModelMixin,
  RetrieveModelMixin,
  CreateModelMixin,
)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer


class ProductListCreateAPIView(ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

  def perform_create(self, serializer):
    title = serializer.validated_data.get('title')
    content = serializer.validated_data.get('content') or None
    if content is None:
      content = title
    serializer.save(content=content)


class ProductDetailAPIView(RetrieveAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer


class ProductUpdateAPIView(UpdateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'

  def perform_update(self, serializer):
    instance = serializer.save()
    if not instance.content:
      instance.content = instance.title


class ProductDeleteAPIView(DestroyAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'

  def perform_destroy(self, instance):
    super().perform_destroy(instance)



# class ProductMixinView(
#   CreateModelMixin,
#   ListModelMixin,
#   RetrieveModelMixin,
#   GenericAPIView,
# ):
#   queryset = Product.objects.all()
#   serializer_class = ProductSerializer
#   lookup_field = 'pk'

#   def get(self, request, *args, **kwargs):
#     pk = kwargs.get('pk')
#     if pk is not None:
#       return self.retrieve(request, *args, **kwargs)
#     return self.list(request, *args, **kwargs)

#   def post(self, request, *args, **kwargs):
#     return self.create(request, *args, **kwargs)

#   def perform_create(self, serializer):
#     content = serializer.validated_data.get('content') or None
#     if content is None:
#       content = 'content updated'
#     serializer.save(content=content)




# @api_view(['GET', 'POST'])
# def product_alt_view(request, pk=None, *args, **kwargs):
#   method = request.method
#   if method == 'GET':
#     if pk is not None:
#       obj = get_object_or_404(Product, pk=pk)
#       data = ProductSerializer(obj, many=False).data
#       return Response(data)
#     queryset = Product.objects.all()
#     data = ProductSerializer(queryset, many=True).data
#     return Response(data)
#   if method == 'POST':
#     serializer = ProductSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#       title = serializer.validated_data.get('title')
#       content = serializer.validated_data.get('content') or None
#       if content is None:
#         content = title
#       serializer.save(content=content)
#       return Response(serializer.data)