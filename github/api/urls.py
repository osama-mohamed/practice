from django.conf.urls import url

from .views import UserAPIView

urlpatterns = [
    url(r'^$', UserAPIView.as_view(), name='home_api'),
]

