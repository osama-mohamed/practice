from django.db import models


class Product(models.Model):
  title = models.CharField(max_length=120)
  slug = models.SlugField()

