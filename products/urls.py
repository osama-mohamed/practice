from django.urls import path
from products.views import (
    product_create_view,
    product_update_view,
    dynamic_product_detail_view,
    product_delete_view,
    product_list_view
)

app_name = 'products'

urlpatterns = [
    path('', product_list_view, name='products_list'),
    path('create/', product_create_view, name='product_create'),
    path('<int:my_id>/', dynamic_product_detail_view, name='product_detail'),
    path('<int:my_id>/update/', product_update_view, name='product_update'),
    path('<int:my_id>/delete/', product_delete_view, name='product_delete'),
]
