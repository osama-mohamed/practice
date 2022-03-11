from django.urls import path

from .views import (
  ProductListCreateAPIView,
  ProductDetailAPIView,
  
  product_alt_view,
)


urlpatterns = [
  path('', ProductListCreateAPIView.as_view()),
  path('<int:pk>/', ProductDetailAPIView.as_view()),
]