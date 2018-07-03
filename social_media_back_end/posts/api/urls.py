from django.conf.urls import url
from .views import (
    NewPostAPIView,
    ProfilePostsAPIView,
    ProfilePostsForUsernameAPIView,
)

urlpatterns = [
    url(r'^new_post/$', NewPostAPIView.as_view(), name='newpost-api'),
    url(r'^profile_posts/$', ProfilePostsAPIView.as_view(), name='profileposts-api'),
    url(r'^profile_posts_for_username/$', ProfilePostsForUsernameAPIView.as_view(), name='profilepostsforusername-api'),
]
