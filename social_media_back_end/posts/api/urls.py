from django.conf.urls import url
from .views import (
    NewPostAPIView,
    ProfilePostsAPIView
)

urlpatterns = [
    url(r'^new_post/', NewPostAPIView.as_view(), name='newpost-api'),
    url(r'^profile_posts/', ProfilePostsAPIView.as_view(), name='profileposts-api'),
]
