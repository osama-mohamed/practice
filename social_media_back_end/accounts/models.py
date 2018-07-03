from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

import os

User = settings.AUTH_USER_MODEL

def get_image_path(instance, filename):

  return os.path.join('user', str(instance.user.id) + '/profile/', filename)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
  if created:
    Token.objects.create(user=instance)


class Account(models.Model):
  user = models.OneToOneField(User, null=True)
  gender = models.CharField(max_length=6, null=True)
  image = models.ImageField(upload_to=get_image_path, null=True)
  activation_key = models.CharField(max_length=120, blank=True, null=True)
  activated = models.BooleanField(default=False)
  added = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.user.username
