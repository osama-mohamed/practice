"""
URL configuration for djviews project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.views.generic import TemplateView, RedirectView

from .views import (
  ProductListView,
  ProductDetailView,
  ProductRedirectView,
  ProductIDRedirectView,
  DigitalProductListView,
  MyProductDetailView,
  ProductCreateView,
)


app_name = 'products_two'

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('digital/', DigitalProductListView.as_view(), name='digital'),
    # path('<int:id>/', ProductDetailView.as_view(), name='detail'),
    path('p/<slug:slug>/', ProductRedirectView.as_view(), name='redirect'),
    path('id/<int:pk>/', ProductIDRedirectView.as_view(), name='redirect_id'),
    path('my/<slug:slug>/', MyProductDetailView.as_view(), name='my_detail'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='detail'),
]
