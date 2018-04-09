from django.conf.urls import url

from .views import AllArticles, NewArticle, UpdateArticle, DeleteArticle

urlpatterns = [
    url(r'^update/(?P<pk>\d+)/$', UpdateArticle.as_view()),
    url(r'^delete/(?P<pk>\d+)/$', DeleteArticle.as_view()),
    url(r'^new/$', NewArticle.as_view()),
    url(r'^all/$', AllArticles.as_view()),
]
