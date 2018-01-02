
from django.conf.urls import url
from home.views import Home
from . import views

# app_name = 'home'

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^friend/(?P<friendship>.+)/(?P<id>\d+)/$', views.change_friends, name='change_friends'),
]
