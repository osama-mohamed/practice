from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


User = settings.AUTH_USER_MODEL


def set_delete_user():
  return get_user_model().objects.get_or_create(username='deleted')[0]


class Car(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET(set_delete_user))
  # user = models.ForeignKey(User, on_delete=models.CASCADE)
  # drivers = models.ManyToManyField(User)
  # first_owner = models.OneToOneField(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=120)

  def __str__(self):
    return self.name
  
# ForeignKey => user_obj.car_set.all() 
# ManyToMany => user_obj.car_set.all()
# OneToOne => user_obj.car