from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
    )

from django.core.urlresolvers import reverse
from django.conf import settings

from products.models import Product


class ProductsSerializer(ModelSerializer):
    detail_url = HyperlinkedIdentityField(
        view_name='products_api:detail_api',
        lookup_field='slug',
    )
    category_url = HyperlinkedIdentityField(
        view_name='products_api:category_api',
        lookup_field='category',
    )
    category = SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'detail_url',
            'category_url',
            'category',
            'name',
            'price',
            'discount',
            'quantity',
            'number_of_sales',
            'number_of_views',
            'avg_rate',
            'description',
            # 'image',
            'slug',
            'added',
            'updated',
        ]

    def get_category(self, obj):
        return str(obj.category)


class ProductDetailSerializer(ModelSerializer):
    category = SerializerMethodField(read_only=True)
    all_products_url = SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'all_products_url',
            'id',
            'category',
            'name',
            'price',
            'discount',
            'quantity',
            'number_of_sales',
            'number_of_views',
            'avg_rate',
            'description',
            # 'image',
            'avg_rate',
            'slug',
            'added',
            'updated',
        ]

    def get_category(self, obj):
        return str(obj.category)

    def get_all_products_url(self, obj):
        return settings.BASE_URL + reverse('products_api:all_api')


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'id',
            'category',
            'name',
            'price',
            'discount',
            'quantity',
            'description',
            'added',
            'updated',
            # 'image',
        ]
