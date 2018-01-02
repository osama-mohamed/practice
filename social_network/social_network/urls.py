
from django.conf.urls import url, include
from django.contrib import admin
from . import views as social_network
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', social_network.login_redirect, name='login_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('accounts.urls', namespace='accounts')),
    url(r'^home/', include('home.urls', namespace='home')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
