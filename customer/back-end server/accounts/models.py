from django.db import models
from django.core.urlresolvers import reverse


class Account(models.Model):
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    country = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(default='default.png', blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('accounts:update', kwargs={'pk': self.id})
