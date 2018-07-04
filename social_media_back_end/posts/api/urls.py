from django.conf.urls import url
from .views import (
    NewPostAPIView,
    ProfilePostsAPIView,
    ProfilePostsForUsernameAPIView,
    DeleteProfilePostAPIView,
)

urlpatterns = [
    url(r'^new_post/$', NewPostAPIView.as_view(), name='newpost-api'),
    url(r'^profile_posts/$', ProfilePostsAPIView.as_view(), name='profileposts-api'),
    url(r'^profile_posts_for_username/$', ProfilePostsForUsernameAPIView.as_view(), name='profilepostsforusername-api'),
    url(r'^delete_profile_post/$', DeleteProfilePostAPIView.as_view(), name='deleteprofilepost-api'),
]
