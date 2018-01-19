from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from restaurants.models import RestaurantLocation


User = settings.AUTH_USER_MODEL


class Item(models.Model):
    user = models.ForeignKey(User)
    restaurant = models.ForeignKey(RestaurantLocation)
    name = models.CharField(max_length=120)
    contents = models.TextField(help_text='Separate by comma!')
    excludes = models.TextField(null=True, blank=True, help_text='Separate by comma!')
    public = models.BooleanField(default=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_contents(self):
        return self.contents.split(',')

    def get_excludes(self):
        return self.excludes.split(',')

    def get_absolute_url(self):
        return reverse('menus:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-updated', '-added']

