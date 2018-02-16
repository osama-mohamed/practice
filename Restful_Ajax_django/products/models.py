from django.db import models
from django.db.models.signals import pre_save
from django.core.urlresolvers import reverse

from .utils import create_slug


class Product(models.Model):
    category = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, null=True)
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    discount = models.FloatField(default=0, blank=True, null=True)
    number_of_sales = models.PositiveIntegerField(default=0, blank=True, null=True)
    number_of_views = models.PositiveIntegerField(default=0, blank=True, null=True)
    avg_rate = models.FloatField(default=0, blank=True, null=True)
    description = models.TextField()
    # image = models.ImageField()
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'slug': self.slug})



def pre_save_post_reciver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_reciver, sender=Product)