from rest_framework.pagination import PageNumberPagination


class ArticlesPageNumberPagination(PageNumberPagination):
    page_size = 1
