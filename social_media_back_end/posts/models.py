import os
from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL

def get_image_path(instance, filename):
  print(filename)
  print(instance)
  print(instance.user.username)
  print(instance.user.id)
  return os.path.join('user', str(instance.user.id), filename)

class Posts(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.CharField(max_length=1000, null=False)
  image = models.ImageField(upload_to=get_image_path, null=True)
  sound = models.CharField(max_length=1000, null=True)
  video = models.CharField(max_length=1000, null=True)
  added = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.user.username
