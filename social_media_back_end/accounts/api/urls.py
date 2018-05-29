from django.conf.urls import url
from .views import (
    SignInAPIView,
)

urlpatterns = [
    url(r'^signup/', SignInAPIView.as_view(), name='signin-api'),
]
