from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django.db.models.signals import post_save

import re

from hashtags.signals import parsed_hashtags
from .validators import validate_content


class TweetManager(models.Manager):
  def retweet(self, user, parent_obj):
    if parent_obj.parent:
      org_parent = parent_obj.parent
    else:
      org_parent = parent_obj
    qs = self.get_queryset().filter(user=user, parent=org_parent)
    # .filter(timestamp__year=timezone.now().year,
    #         timestamp__month=timezone.now().month, timestamp__day=timezone.now().day)
    if qs.exists():
      return None
    obj = self.model(
      parent = org_parent,
      user = user,
      content = parent_obj.content,
    )
    obj.save()
    return obj


class Tweet(models.Model):
  parent = models.ForeignKey("self", blank=True, null=True)
  user = models.ForeignKey(settings.AUTH_USER_MODEL)
  content = models.CharField(max_length=140, validators=[validate_content])
  updated = models.DateTimeField(auto_now=True)
  timestamp = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['-timestamp']

  objects = TweetManager()

  def __str__(self):
    return str(self.content)

  def get_absolute_url(self):
    return reverse('tweet:detail', kwargs={'pk': self.pk})
  
  def get_absolute_update_url(self):
    return reverse('tweet:update', kwargs={'pk': self.pk})
  
  def get_absolute_delete_url(self):
    return reverse('tweet:delete', kwargs={'pk': self.pk})


def tweet_save_receiver(sender, instance, created, *args, **kwargs):
  if created and not instance.parent:
    # notify a user
    user_regex = r'@(?P<username>[\w.@+-]+)'
    usernames = re.findall(user_regex, instance.content)
    # send notification to user.
    hash_regex = r'#(?P<hashtag>[\w\d-]+)'
    hashtags = re.findall(hash_regex, instance.content)
    parsed_hashtags.send(sender=instance.__class__, hashtag_list=hashtags)
    # send hashtag signal to user.

post_save.connect(tweet_save_receiver, sender=Tweet)
