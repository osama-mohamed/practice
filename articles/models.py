from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=220)
  slug = models.SlugField(blank=True, null=True)
  content = models.TextField()
  timestamp = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  publish = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)

def slugify_instance_title(instance, save=False):
  slug = slugify(instance.title)
  qs = Article.objects.filter(slug=slug).exclude(id=instance.id)
  if qs.exists():
    slug = f'{slug}-{qs.count() + 1}'
  instance.slug = slug
  if save:
    instance.save()
  return instance

def article_pre_save(sender, instance, *args, **kwargs):
  if instance.slug is None:
    slugify_instance_title(instance, save=False)
pre_save.connect(article_pre_save, sender=Article)


def article_post_save(sender, instance, created, *args, **kwargs):
  if created:
    slugify_instance_title(instance, save=True)
post_save.connect(article_post_save, sender=Article)