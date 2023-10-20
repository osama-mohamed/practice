from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class Product(models.Model):
  user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='products_two')
  title = models.CharField(max_length=120)
  slug = models.SlugField(unique=True)

class DigitalProduct(Product):
  class Meta:
    proxy = True # use product table without creating a new DB table