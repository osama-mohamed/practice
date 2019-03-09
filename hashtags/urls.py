from django.conf.urls import url

from .views import (
  HashTagView,
)


urlpatterns = [
  url(r'^(?P<hashtag>.*)/$', HashTagView.as_view(), name='list'),
]