from django.conf.urls import url
from .views import (
    RegisterAPIView,
    ProfileAPIView,
    ProfileUpdateAPIView,
    ProfileDeleteAPIView,
    AllUsersAPIView
)

urlpatterns = [
    url(r'^register/', RegisterAPIView.as_view(), name='register_api'),
    url(r'^users/all/$', AllUsersAPIView.as_view(), name='change_password_api'),
    url(r'^profile/(?P<id>\d+)/$', ProfileAPIView.as_view(), name='profile_api'),
    url(r'^profile/update/(?P<id>\d+)/$', ProfileUpdateAPIView.as_view(), name='update_api'),
    url(r'^profile/delete/(?P<id>\d+)/$', ProfileDeleteAPIView.as_view(), name='delete_api'),
]
