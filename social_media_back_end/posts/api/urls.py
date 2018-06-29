from django.conf.urls import url
from .views import (
    NewPostAPIView
)

urlpatterns = [
    url(r'^new_post/', NewPostAPIView.as_view(), name='newpost-api'),
]
