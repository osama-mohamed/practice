from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


User = settings.AUTH_USER_MODEL


def set_delete_user():
  return get_user_model().objects.get_or_create(username='deleted')[0]


def limit_car_choices():
  Q = models.Q
  return Q(username__icontains='o')

class Car(models.Model):
  user = models.ForeignKey(
    User, 
    on_delete=models.SET(set_delete_user), 
    limit_choices_to={"is_staff": True},
    # limit_choices_to = limit_car_choices,
  )
  # user = models.ForeignKey(User, on_delete=models.CASCADE)
  # drivers = models.ManyToManyField(User)
  # first_owner = models.OneToOneField(User, on_delete=models.CASCADE)
  updated_by = models.ForeignKey(User, related_name='updated_car_user', null=True, blank=True, on_delete=models.SET_NULL) 
  name = models.CharField(max_length=120)

  def __str__(self):
    return self.name
  

# https://docs.djangoproject.com/en/4.2/ref/models/fields/#module-django.db.models.fields.related
# ForeignKey => user_obj.car_set.all() OR user_obj.updated_car_user.all()
# ManyToMany => user_obj.car_set.all()
# OneToOne => user_obj.car