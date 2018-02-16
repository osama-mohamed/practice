from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from products.views import HomeListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/accounts/', include('accounts.api.urls', namespace='accounts_api')),
    url(r'^api/products/', include('products.api.urls', namespace='products_api')),
    url(r'^$', HomeListView.as_view(), name='main_home'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
