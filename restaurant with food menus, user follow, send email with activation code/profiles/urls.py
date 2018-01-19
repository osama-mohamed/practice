from django.conf.urls import url
from .views import (
    ProfileDetailView,
    ProfileFollowToggle,
)

urlpatterns = [
    url(r'^(?P<username>[\w-]+)/$', ProfileDetailView.as_view(), name='detail'),
    # url(r'^profile-follow/$', ProfileFollowToggle.as_view(), name='follow'),
]
