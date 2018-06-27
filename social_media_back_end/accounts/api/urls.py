from django.conf.urls import url
from .views import (
    CheckUsernameAPIView,
    SignUpAPIView,
    SignInAPIView,
    ProfileAPIView
)

urlpatterns = [
    url(r'^checkusername/', CheckUsernameAPIView.as_view(), name='checkusername-api'),
    url(r'^signup/', SignUpAPIView.as_view(), name='signup-api'),
    url(r'^signin/', SignInAPIView.as_view(), name='signin-api'),
    url(r'^profile/', ProfileAPIView.as_view(), name='profile-api'),
]
