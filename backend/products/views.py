from rest_framework.generics import (
  RetrieveAPIView,
  CreateAPIView,
)

from .models import Product
from .serializers import ProductSerializer

# Create your views here.

class ProductCreateAPIView(CreateAPIView):
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
