from rest_framework.generics import RetrieveAPIView

from .models import Product
from .serializers import ProductSerializer

# Create your views here.

class ProductDetailAPIView(RetrieveAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
