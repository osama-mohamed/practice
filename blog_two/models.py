from django.db import models
from django.db.models.signals import pre_save, post_save

from django.utils import timezone
from django.utils.timesince import timesince
from django.utils.encoding import smart_str
from django.utils.text import slugify

from datetime import timedelta, datetime, date


from .validators import validate_author_email


PUBLISH_CHOICES = [
  ('DR', 'Draft'),
  ('PU', 'Publish'),
  ('PR', 'Private'),
]


class Post(models.Model):
  active = models.BooleanField(default=True)
  title = models.CharField(
    max_length=240,
    verbose_name='Post Title',
    unique=True,
    error_messages={
      'unique': 'This title is not unique, please try again.', # docs.djangoproject.com/en/4.2/ref/models/fields/#django.db.models.Field.error_messages
    },
    help_text='Must be a unique title.',
  )
  slug = models.SlugField(null=True, blank=True)
  content = models.TextField(null=True, blank=True)
  publish = models.CharField(max_length=120, choices=PUBLISH_CHOICES, default='draft')# docs.djangoproject.com/en/4.2/ref/models/fields/#choices
  view_count = models.IntegerField(default=0)
  publish_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
  author_email = models.EmailField(max_length=240, validators=[validate_author_email,], null=True, blank=True)
  timestamp = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  class Mete:
    verbose_name = 'Post'
    verbose_name_plural = 'Posts'

  def __str__(self):
    return smart_str(self.title) # docs.djangoproject.com/en/4.2/ref/unicode/#useful-utility-functions
  
  def save(self, *args, **kwargs):
    # if not self.slug:
    #   self.slug = slugify(self.title, allow_unicode=True) # allow_unicode=True for non-english languages => docs.djangoproject.com/en/4.2/ref/utils/#django.utils.text.slugify
    super(Post, self).save(*args, **kwargs)

  def publish_from_time(self):

    return timesince(self.publish_date) # docs.djangoproject.com/en/4.2/ref/utils/#django.utils.timesince.timesince

  @property
  def other_publish_time(self):
    if self.publish == 'PU':
      now = datetime.now()
      publish_time = datetime.combine(
        self.publish_date,
        datetime.now().min.time()
      )
      try:
        difference = now - publish_time
      except:
        return 'Unknown'
      if difference <= timedelta(minutes=1):
        return 'Just now'
      return f'{timesince(publish_time).split(', ')[0]} ago'
    return 'Not published'


def post_pre_save_receiver(sender, instance, *args, **kwargs): # docs.djangoproject.com/en/4.2/ref/signals/#pre-save
  if not instance.slug and instance.title:
    instance.slug = slugify(instance.title, allow_unicode=True)
  

def post_post_save_receiver(sender, instance, created, *args, **kwargs): # docs.djangoproject.com/en/4.2/ref/signals/#post-save
  if created:
    if not instance.slug and instance.title:
      instance.slug = slugify(instance.title, allow_unicode=True)
      instance.save()


pre_save.connect(post_pre_save_receiver, sender=Post)
post_save.connect(post_post_save_receiver, sender=Post)