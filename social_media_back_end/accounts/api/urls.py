from django.conf.urls import url
from .views import (
    SignUpAPIView,
    SignInAPIView
)

urlpatterns = [
    url(r'^signup/', SignUpAPIView.as_view(), name='signup-api'),
    url(r'^signin/', SignInAPIView.as_view(), name='signin-api'),
]
