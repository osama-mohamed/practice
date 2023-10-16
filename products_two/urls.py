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

# from .views import (
# #   AboutUsView,
# )
app_name = 'products_two'

urlpatterns = [
    # path('about_us/', AboutUsView.as_view(), name='about_us'),
    path('about_us/', TemplateView.as_view(template_name='about.html'), name='about_us'),
    path('redirect/', RedirectView.as_view(url='https://github.com/osama-mohamed'), name='redirect'),
]
