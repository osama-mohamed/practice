from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.serializers import (
  ModelSerializer,
  SerializerMethodField,
  HyperlinkedIdentityField,
)

User = get_user_model()


class UserDisplaySerializer(ModelSerializer):
  followers_count = SerializerMethodField()
  user_url = HyperlinkedIdentityField(
    view_name='profiles:detail',
    lookup_field='username',
  )
  follow_url = HyperlinkedIdentityField(
    view_name='profiles:follow',
    lookup_field='username',
  )

  class Meta:
    model = User
    fields = [
      'username',
      'first_name',
      'last_name',
      'followers_count',
      'email',
      'user_url',
      'follow_url',
    ]

  def get_followers_count(self, obj):
    return obj.followed_by.all().count()
