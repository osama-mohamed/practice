from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL


class Car(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=120)

  def __str__(self):
    return self.name