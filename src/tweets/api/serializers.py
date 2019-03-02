from rest_framework.serializers import (
  ModelSerializer,
  SerializerMethodField,
  HyperlinkedIdentityField
)
from django.urls import reverse
from django.utils.timesince import timesince

from accounts.api.serializers import UserDisplaySerializer
from tweets.models import Tweet


class TweetModelSerializer(ModelSerializer):
  user = UserDisplaySerializer(read_only=True)
  date_display = SerializerMethodField()
  timesince = SerializerMethodField()
  id = SerializerMethodField()
  owner = SerializerMethodField()
  view_url = HyperlinkedIdentityField(
    view_name='tweet:detail',
    # lookup_field='pk',
  )
  update_url = HyperlinkedIdentityField(
    view_name='tweet:update',
    # lookup_field='pk',
  )
  delete_url = HyperlinkedIdentityField(
    view_name='tweet:delete',
    # lookup_field='pk',
  )
  
  class Meta:
    model = Tweet
    fields = [
      'user',
      'content',
      'timestamp',
      'date_display',
      'timesince',
      'id',
      'owner',
      'view_url',
      'update_url',
      'delete_url',
    ]
  
  def get_date_display(self, obj):
    return obj.timestamp.strftime("%b %d, %Y at %I:%M %p")

  def get_timesince(self, obj):
    return timesince(obj.timestamp) + " ago"
  
  def get_id(self, obj):
    return obj.id
  
  def get_owner(self, obj):
    tweet_owner = obj.user.username
    current_user = self.context['request'].user.username
    if tweet_owner == current_user:
      return True
    return False
