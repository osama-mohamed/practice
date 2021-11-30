from django.conf import settings
from django.db import models

from .validators import validate_unit_of_measure
# Create your models here.

class Recipe(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  name = models.CharField(max_length=220)
  description = models.TextField(blank=True, null=True)
  directions = models.TextField(blank=True, null=True)
  active = models.BooleanField(default=True)
  timestamp = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)


class RecipeIngredient(models.Model):
  recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
  name = models.CharField(max_length=220)
  quantity = models.CharField(max_length=50)
  unit = models.CharField(max_length=50, validators=[validate_unit_of_measure,])
  description = models.TextField(blank=True, null=True)
  directions = models.TextField(blank=True, null=True)
  active = models.BooleanField(default=True)
  timestamp = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
