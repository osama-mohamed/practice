from django.conf.urls import url

from django.views.generic.base import RedirectView

from .views import (
  TweetCreateAPIView,
  TweetListAPIView,
  RetweetAPIView,
)


urlpatterns = [
  url(r'^$', TweetListAPIView.as_view(), name='list'),
  url(r'^create/$', TweetCreateAPIView.as_view(), name='create'),
  url(r'^(?P<pk>\d+)/retweet/$', RetweetAPIView.as_view(), name='retweet'),
  # url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'),
  # url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'),
  # url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'),
]
