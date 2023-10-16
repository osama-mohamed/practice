from django.db import models

from django.utils import timezone
from django.utils.encoding import smart_str
from django.utils.text import slugify


from .validators import validate_author_email
  

PUBLISH_CHOICES = [
  ('DR', 'Draft'),
  ('PU', 'Publish'),
  ('PR', 'Private'),
]


class Post(models.Model):
  active = models.BooleanField(default=True)
  title = models.CharField(max_length=240, verbose_name='Post Title', unique=True)
  slug = models.SlugField(null=True, blank=True)
  content = models.TextField(null=True, blank=True)
  publish = models.CharField(max_length=120, choices=PUBLISH_CHOICES, default='draft')# docs.djangoproject.com/en/4.2/ref/models/fields/#choices
  view_count = models.IntegerField(default=0)
  publish_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
  author_email = models.EmailField(max_length=240, validators=[validate_author_email,], null=True, blank=True)

  class Mete:
    verbose_name = 'Post'
    verbose_name_plural = 'Posts'

  def __str__(self):
    return smart_str(self.title) # docs.djangoproject.com/en/4.2/ref/unicode/#useful-utility-functions
  
  def save(self, *args, **kwargs):
    if not self.slug:
      print(self.slug)
      self.slug = slugify(self.title, allow_unicode=True) # allow_unicode=True for non-english languages => docs.djangoproject.com/en/4.2/ref/utils/#django.utils.text.slugify
    super(Post, self).save(*args, **kwargs)
