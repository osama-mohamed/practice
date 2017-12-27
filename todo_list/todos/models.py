from django.db import models
from datetime import datetime
# from __future__ import unicode_literals


class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.title
