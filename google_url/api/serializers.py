from rest_framework.serializers import (
    Serializer,
    CharField,
)


class UrlSerializer(Serializer):
    url = CharField(max_length=500)
