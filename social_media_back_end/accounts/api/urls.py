from django.conf.urls import url
from .views import (
    CheckUsernameAPIView,
    SignUpAPIView,
    SignInAPIView
)

urlpatterns = [
    url(r'^checkusername/', CheckUsernameAPIView.as_view(), name='checkusername-api'),
    url(r'^signup/', SignUpAPIView.as_view(), name='signup-api'),
    url(r'^signin/', SignInAPIView.as_view(), name='signin-api'),
]
