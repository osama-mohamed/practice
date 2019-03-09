from rest_framework.serializers import (
  ModelSerializer,
  SerializerMethodField,
  HyperlinkedIdentityField,
  CharField,
)
from django.urls import reverse
from django.utils.timesince import timesince

from accounts.api.serializers import UserDisplaySerializer
from tweets.models import Tweet


class ParentTweetModelSerializer(ModelSerializer):
  user = UserDisplaySerializer(read_only=True)
  date_display = SerializerMethodField()
  timesince = SerializerMethodField()
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
  retweet_url = HyperlinkedIdentityField(
    view_name='tweet:retweet',
    # lookup_field='pk',
  )
  api_retweet_url = HyperlinkedIdentityField(
    view_name='tweet-api:retweet',
  )
  likes = SerializerMethodField()
  did_like = SerializerMethodField()

  class Meta:
    model = Tweet
    fields = [
      'id',
      'user',
      'content',
      'timestamp',
      'date_display',
      'timesince',
      'view_url',
      'update_url',
      'delete_url',
      'retweet_url',
      'api_retweet_url',
      'likes',
      'did_like',
    ]

  def get_date_display(self, obj):
    return obj.timestamp.strftime("%b %d, %Y at %I:%M %p")

  def get_timesince(self, obj):
    return timesince(obj.timestamp) + " ago"

  def get_did_like(self, obj):
    request = self.context.get("request")
    try:
      user = request.user
      if user.is_authenticated():
        if user in obj.liked.all():
          return True
    except:
      pass
    return False

  def get_likes(self, obj):
    return obj.liked.all().count()


class TweetModelSerializer(ModelSerializer):
  parent_id = CharField(write_only=True, required=False)
  user = UserDisplaySerializer(read_only=True)
  date_display = SerializerMethodField()
  timesince = SerializerMethodField()
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
  retweet_url = HyperlinkedIdentityField(
    view_name='tweet:retweet',
    # lookup_field='pk',
  )
  api_retweet_url = HyperlinkedIdentityField(
    view_name='tweet-api:retweet',
  )
  is_retweet = SerializerMethodField()
  parent = ParentTweetModelSerializer(read_only=True)
  likes = SerializerMethodField()
  did_like = SerializerMethodField()
  
  class Meta:
    model = Tweet
    fields = [
      'parent_id',
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
      'retweet_url',
      'api_retweet_url',
      'is_retweet',
      'parent',
      'likes',
      'did_like',
      'reply',
    ]
  
  def get_date_display(self, obj):
    return obj.timestamp.strftime("%b %d, %Y at %I:%M %p")

  def get_timesince(self, obj):
    return timesince(obj.timestamp) + " ago"
  
  def get_owner(self, obj):
    tweet_owner = obj.user.username
    current_user = self.context['request'].user.username
    if tweet_owner == current_user:
      return True
    return False
  
  def get_is_retweet(self, obj):
    if obj.parent:
      return True
    return False

  def get_did_like(self, obj):
    request = self.context.get("request")
    try:
      user = request.user
      if user.is_authenticated():
        if user in obj.liked.all():
          return True
    except:
      pass
    return False

  def get_likes(self, obj):
    return obj.liked.all().count()
