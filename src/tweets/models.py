from django.db import models
from django.conf import settings
from django.urls import reverse
from .validators import validate_content


class Tweet(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL)
  content = models.CharField(max_length=140, validators=[validate_content])
  updated = models.DateTimeField(auto_now=True)
  timestamp = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['-timestamp']

  def __str__(self):
    return str(self.content)

  def get_absolute_url(self):
    return reverse('tweet:detail', kwargs={'pk': self.pk})
  
  def get_absolute_update_url(self):
    return reverse('tweet:update', kwargs={'pk': self.pk})
  
  def get_absolute_delete_url(self):
    return reverse('tweet:delete', kwargs={'pk': self.pk})
