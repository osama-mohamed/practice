from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', include('google_url.urls', namespace='google_url')),
    url(r'^api/$', include('google_url.api.urls', namespace='google_url_api')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
