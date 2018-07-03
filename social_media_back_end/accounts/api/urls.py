from django.conf.urls import url
from .views import (
    CheckUsernameAPIView,
    SignUpAPIView,
    SignInAPIView,
    SignOutAPIView,
    ProfileAPIView,
    ProfilePicAPIView
)

urlpatterns = [
    url(r'^checkusername/$', CheckUsernameAPIView.as_view(), name='checkusername-api'),
    url(r'^signup/$', SignUpAPIView.as_view(), name='signup-api'),
    url(r'^signin/$', SignInAPIView.as_view(), name='signin-api'),
    url(r'^signout/$', SignOutAPIView.as_view(), name='signout-api'),
    url(r'^profile/$', ProfileAPIView.as_view(), name='profile-api'),
    url(r'^profile_pic/$', ProfilePicAPIView.as_view(), name='profilepic-api'),
]
