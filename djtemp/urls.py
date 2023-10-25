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
from django.urls import path

from .views import (
    some_test_view,
    post_model_list_view,
    
    post_model_create_view,
    post_model_detail_view,
    post_model_delete_view,
    post_model_update_view,
    )


app_name = 'djtemp'

urlpatterns = [
  path('', post_model_list_view, name='list'),
  path('test/', some_test_view, name='test'),
  path('create/', post_model_create_view, name='create'),
  path('<int:id>/', post_model_detail_view, name='detail'),
  path('<int:id>/update/', post_model_update_view, name='update'),
  path('<int:id>/delete/', post_model_delete_view, name='delete'),
]
