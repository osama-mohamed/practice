from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class ProductLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20
    max_limit = 50


class ProductPageNumberPagination(PageNumberPagination):
    page_size = 20
