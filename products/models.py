from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify


from .validators import validate_blocked_words


User = settings.AUTH_USER_MODEL

class ProductQueryset(models.QuerySet):
  def published(self): # Product.objects.filter().published() & Product.objects.published()
    return self.filter(state=Product.ProductStateOptions.PUBLISH, publish_timestamp__lte=timezone.now())


class ProductManager(models.Manager):
  def get_queryset(self):
    return ProductQueryset(self.model, using=self._db)
  
  def published(self): # Product.objects.published()
    return self.get_queryset().published()
  
class Product(models.Model):
  class ProductStateOptions(models.TextChoices):
    PUBLISH = 'PU', 'Published'
    DRAFT = 'DR', 'Draft'
    PRIVATE = 'PR', 'Private'
    # obj.get_state_display()
    # state=Product.productstateoptions.PUBLISH

  user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
  title = models.CharField(max_length=120, validators=[validate_blocked_words]) # unique=True
  slug = models.SlugField(blank=True, unique=True, null=True, db_index=True)
  state = models.CharField(max_length=2, default=ProductStateOptions.DRAFT,
                           choices=ProductStateOptions.choices)
  description = models.TextField(null=True)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  publish_timestamp = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)
  timestamp = models.DateTimeField(auto_now_add=True) # default=timezone.now
  updated = models.DateTimeField(auto_now=True)

  objects = ProductManager()

  class Meta:
    ordering = ['-updated', '-timestamp']
    # verbose_name = 'Product' # fix model class name 
    # verbose_name_plural = 'Products' # fix model class name showen to user
    # unique_together = [['title', 'id']]
    # db_table = 'products_product'

  def __str__(self):
    return self.title

  def save(self, *args, **kwargs):
    validate_blocked_words(self.title)
    if self.state_is_published and self.publish_timestamp is None:
      self.publish_timestamp = timezone.now()
    else:
      self.publish_timestamp = None
    super().save(*args, **kwargs)

  def get_absolute_url(self):
    return reverse('products:detail', kwargs={'id': self.id})
  def get_absolute_slug_url(self):
    return reverse('products:detail_slug', kwargs={'slug': self.slug})

  @property
  def state_is_published(self):
    return self.state == self.ProductStateOptions.PUBLISH
  
  @property
  def is_published(self):
    publish_timestamp = self.publish_timestamp
    return self.state_is_published and publish_timestamp < timezone.now()
  # def is_published(self):
  #   return self.state == self.ProductStateOptions.PUBLISH



def slugify_pre_save(sender, instance, *args, **kwargs):
  if not instance.slug:
    # instance.slug = slugify(instance.title)
    new_slug = slugify(instance.title)
    klass = instance.__class__ # sender
    qs = klass.objects.filter(slug=new_slug) # .exclude(id=instance.id)
    if qs.count() == 0:
      instance.slug = new_slug
    else:
      instance.slug = f'{new_slug}-{qs.count()}'
    

pre_save.connect(slugify_pre_save, sender=Product)