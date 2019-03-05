from django.conf.urls import url

from django.views.generic.base import RedirectView

from .views import (
  TweetCreateAPIView,
  TweetListAPIView,
  RetweetAPIView,
  LikeToggleAPIView,
)


urlpatterns = [
  url(r'^$', TweetListAPIView.as_view(), name='list'),
  url(r'^create/$', TweetCreateAPIView.as_view(), name='create'),
  url(r'^(?P<pk>\d+)/retweet/$', RetweetAPIView.as_view(), name='retweet'),
  url(r'^(?P<pk>\d+)/like/$', LikeToggleAPIView.as_view(), name='like-toggle'),
]
