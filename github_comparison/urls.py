from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('github.api.urls', namespace='github_detail_api')),
    url(r'^$', include('github.urls', namespace='github_detail')),
]

