from django.db import models
from django.urls import reverse
from django.conf import settings


def upload_location(instance, filename):
  PostModel = instance.__class__
  new_id = PostModel.objects.order_by('id').last().id + 1
  return f'{new_id}/{filename}'


class Post(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
  title = models.CharField(max_length=120)
  slug = models.SlugField(unique=True)
  image = models.FileField(upload_to=upload_location, null=True, blank=True)
  height_field = models.IntegerField(default=0)
  width_field = models.IntegerField(default=0)
  content = models.TextField()
  draft = models.BooleanField(default=False)
  publish = models.DateField(auto_now=False, auto_now_add=False)
  updated = models.DateTimeField(auto_now=True, auto_now_add=False)
  timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

  def __str__(self):
    return self.title

  # def get_absolute_url(self):
  #   return reverse('blog_three:detail', kwargs={'slug': self.slug})

  class Meta:
    ordering = ['-timestamp', '-updated']