from django.conf import settings
from django.db import models
from django.urls import reverse

User = settings.AUTH_USER_MODEL


class Product(models.Model):
  user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='products_two')
  title = models.CharField(max_length=120)
  slug = models.SlugField(unique=True)

  def get_absolute_url(self):
    return reverse('products_two:detail', kwargs={'slug': self.slug})

class DigitalProduct(Product):
  class Meta:
    proxy = True # use product table without creating a new DB table