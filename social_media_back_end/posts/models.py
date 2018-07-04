import os
from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.conf import settings


User = settings.AUTH_USER_MODEL

def get_image_path(instance, filename):
  return os.path.join('user', str(instance.user.id), filename)


class Posts(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.CharField(max_length=1000, null=False)
  image = models.ImageField(upload_to=get_image_path, null=True)
  sound = models.CharField(max_length=1000, null=True)
  video = models.CharField(max_length=1000, null=True)
  publish = models.BooleanField(default=True)
  block_comment = models.BooleanField(default=False)
  added = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.user.username


def pre_delete_post_img(sender, instance, *args, **kwargs):
  if instance.image:
    if os.path.isfile(instance.image.path):
      os.remove(instance.image.path)


pre_delete.connect(pre_delete_post_img, sender=Posts)