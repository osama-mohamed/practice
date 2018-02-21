from django.conf.urls import url

from .views import home#, git_user_detail

urlpatterns = [
    url(r'^$', home, name='home'),
    # url(r'^(?P<user>[\w-]+)/$', git_user_detail),
]

