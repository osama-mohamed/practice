from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL


class Posts(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.CharField(max_length=1000, null=False)
  added = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.user.username
