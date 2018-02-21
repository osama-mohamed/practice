from rest_framework.serializers import (
    Serializer,
    CharField,
)


class UserSerializer(Serializer):
    user_name_one = CharField(max_length=200)
    user_name_two = CharField(max_length=200)
