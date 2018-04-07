from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length=250, null=True)
    body = models.TextField(null=True)
    img = models.ImageField(null=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
