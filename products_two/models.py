from django.db import models


class Product(models.Model):
  title = models.CharField(max_length=120)
  slug = models.SlugField()

class DigitalProduct(Product):
  class Meta:
    proxy = True # use product table without creating a new DB table