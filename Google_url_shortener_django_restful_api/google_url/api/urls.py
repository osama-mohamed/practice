from django.conf.urls import url

from .views import UrlAPIView

urlpatterns = [
    url(r'^$', UrlAPIView.as_view(), name='home_api'),
]
