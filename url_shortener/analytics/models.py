from django.db import models
from shortener.models import URL


class ClickEventManager(models.Manager):
    def create_event(self, urlinstance):
        if isinstance(urlinstance, URL):
            obj, created = self.get_or_create(url=urlinstance)
            obj.count += 1
            obj.save()
            return obj.count
        return None


class ClickEvent(models.Model):
    url = models.OneToOneField(URL)
    count = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = ClickEventManager()

    def __str__(self):
        return '{i}'.format(i=self.count)
