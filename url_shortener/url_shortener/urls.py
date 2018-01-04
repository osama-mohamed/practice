from django.conf.urls import url, include
from django.contrib import admin
from shortener.views import RedirectView, HomeView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<shortcode>[\w-]+)/$', RedirectView.as_view(), name='scode'),
    url(r'^$', HomeView.as_view()),
]
