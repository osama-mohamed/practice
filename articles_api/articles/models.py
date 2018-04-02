from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
