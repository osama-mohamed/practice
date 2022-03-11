from django.urls import path

from .views import (
  ProductCreateAPIView,
  ProductDetailAPIView,
)


urlpatterns = [
  path('create/', ProductCreateAPIView.as_view()),
  path('<int:pk>/', ProductDetailAPIView.as_view()),
]