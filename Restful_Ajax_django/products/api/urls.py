from django.conf.urls import url
from .views import (
    AllProductsAPIView,
    ProductDetailAPIView,
    CategoryAPIView,
    AddProductAPIView,
    UpdateProductsAPIView,
    DeleteProductsAPIView,
)

urlpatterns = [
    url(r'^category/(?P<category>[a-zA-Z0-9].*)/$', CategoryAPIView.as_view(), name='category_api'),
    url(r'^all/$', AllProductsAPIView.as_view(), name='all_api'),
    url(r'^add/$', AddProductAPIView.as_view(), name='add_api'),
    url(r'^update/(?P<id>\d+)/$', UpdateProductsAPIView.as_view(), name='update_api'),
    url(r'^delete/(?P<id>\d+)/$', DeleteProductsAPIView.as_view(), name='delete_api'),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailAPIView.as_view(), name='detail_api'),
]
