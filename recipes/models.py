from django.conf import settings
from django.db import models

from .utils import number_str_to_float
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
  quantity_as_float = models.FloatField(blank=True, null=True)
  unit = models.CharField(max_length=50, validators=[validate_unit_of_measure,])
  description = models.TextField(blank=True, null=True)
  directions = models.TextField(blank=True, null=True)
  active = models.BooleanField(default=True)
  timestamp = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def save(self, *args, **kwargs):
    qty = self.quantity
    qty_as_float, qty_as_float_success = number_str_to_float(qty)
    if qty_as_float_success:
      self.quantity_as_float = qty_as_float
    else:
      self.quantity_as_float = None
    super().save(*args, **kwargs)
