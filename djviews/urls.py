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

from .views import redirect_somewhere
urlpatterns = [
    path('admin/', admin.site.urls),
    path('redirect/', redirect_somewhere, name='redirect'),
    path('blog/', include('blog.urls', namespace='blog')),
    path('blog_two/', include('blog_two.urls', namespace='blog_two')),
    path('products/', include('products.urls', namespace='products')),
    path('products_two/', include('products_two.urls', namespace='products_two')),
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
    path('blog_three/', include('blog_three.urls', namespace='blog_three')),
    path('djtemp/', include('djtemp.urls', namespace='djtemp')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
]
