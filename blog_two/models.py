from django.db import models


PUBLISH_CHOICES = [
  ('DR', 'Draft'),
  ('PU', 'Publish'),
  ('PR', 'Private'),
]


class Post(models.Model):
  active = models.BooleanField(default=True)
  title = models.CharField(max_length=240, verbose_name='Post Title')
  content = models.TextField(null=True, blank=True)
  publish = models.CharField(max_length=120, choices=PUBLISH_CHOICES, default='draft')

  class Mete:
    verbose_name = 'Post'
    verbose_name_plural = 'Posts'

  def __str__(self):
    return self.title