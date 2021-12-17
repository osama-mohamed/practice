from django.conf import settings
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from .utils import slugify_instance_title

# Create your models here.

User = settings.AUTH_USER_MODEL

class ArticleQuerySet(models.QuerySet):
  def search(self, query=None):
    if query is None or query == '':
      return self.none()
    return self.filter(
      Q(title__icontains=query) |
      Q(content__icontains=query)
    )

class ArticleManager(models.Manager):

  def get_queryset(self):
    return ArticleQuerySet(self.model, using=self._db)
    
  def search(self, query=None):
    # if query is None or query == '':
    #   return self.get_queryset().none()
    # return self.get_queryset().filter(
    #   Q(title__icontains=query) |
    #   Q(content__icontains=query)
    # )
    return self.get_queryset().search(query=query)


class Article(models.Model):
  user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
  title = models.CharField(max_length=220)
  slug = models.SlugField(unique=True, blank=True, null=True)
  content = models.TextField()
  timestamp = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  publish = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)

  objects = ArticleManager()

  @property
  def name(self):
    return self.title

  def get_absolute_url(self):
    return reverse('articles:detail', kwargs={'slug': self.slug})
  
  def get_edit_url(self):
    return reverse('articles:update', kwargs={'slug': self.slug})
  
  def get_delete_url(self):
    return reverse('articles:delete', kwargs={'slug': self.slug})


def article_pre_save(sender, instance, *args, **kwargs):
  if instance.slug is None:
    slugify_instance_title(instance, save=False)
pre_save.connect(article_pre_save, sender=Article)


def article_post_save(sender, instance, created, *args, **kwargs):
  if created:
    slugify_instance_title(instance, save=True)
post_save.connect(article_post_save, sender=Article)