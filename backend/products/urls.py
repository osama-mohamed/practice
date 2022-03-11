from django.urls import path

from .views import (
  ProductListCreateAPIView,
  ProductDetailAPIView,
  ProductUpdateAPIView,
  ProductDeleteAPIView,

  product_alt_view,
)


urlpatterns = [
  path('', ProductListCreateAPIView.as_view()),
  path('<int:pk>/update/', ProductUpdateAPIView.as_view()),
  path('<int:pk>/delete/', ProductDeleteAPIView.as_view()),
  path('<int:pk>/', ProductDetailAPIView.as_view()),
]