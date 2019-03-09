from django.conf.urls import url, include
from django.views.generic import RedirectView

from .views import (
  TweetCreateView,
  TweetDetailView,
  TweetListView,
  TweetUpdateView,
  TweetDeleteView,
  RetweetView,
)


urlpatterns = [
  url(r'^$', RedirectView.as_view(url='/'), name='list'),
  url(r'^search/$', TweetListView.as_view(), name='search'),
  url(r'^create/$', TweetCreateView.as_view(), name='create'),
  url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'),
  url(r'^(?P<pk>\d+)/retweet/$', RetweetView.as_view(), name='retweet'),
  url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'),
  url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'),
]