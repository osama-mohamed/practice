from rest_framework.serializers import ModelSerializer

from accounts.models import Account


class ProfileSerializer(ModelSerializer):

    class Meta:
        model = Account
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
            'country',
            'image',
            'region',
            'address',
            'phone_number',
            'added',
            'updated'
        ]
