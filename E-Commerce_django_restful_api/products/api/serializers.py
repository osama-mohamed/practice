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
    user = SerializerMethodField(read_only=True)
    category = SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'detail_url',
            'category_url',
            'user',
            'category',
            'name',
            'price',
            'discount',
            'quantity',
            'number_of_sales',
            'number_of_views',
            'avg_rate',
            'description',
            'image',
            'avg_rate',
            'slug',
            'slider',
            'publish',
            'block_review',
            'added',
            'updated',
        ]

    def get_user(self, obj):
        return str(obj.user)

    def get_category(self, obj):
        return str(obj.category)


class ProductDetailSerializer(ModelSerializer):
    user = SerializerMethodField(read_only=True)
    category = SerializerMethodField(read_only=True)
    all_products_url = SerializerMethodField()
    add_review_url = HyperlinkedIdentityField(
        view_name='reviews_api:add_api',
        lookup_field='id',
    )

    class Meta:
        model = Product
        fields = [
            'all_products_url',
            'add_review_url',
            'id',
            'user',
            'category',
            'name',
            'price',
            'discount',
            'quantity',
            'number_of_sales',
            'number_of_views',
            'avg_rate',
            'description',
            'image',
            'avg_rate',
            'slug',
            'slider',
            'publish',
            'block_review',
            'added',
            'updated',
        ]

    def get_user(self, obj):
        return str(obj.user)

    def get_category(self, obj):
        return str(obj.category)

    def get_all_products_url(self, obj):
        return settings.BASE_URL + reverse('products_api:list_api')
