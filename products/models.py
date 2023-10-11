from django.db import models
from django.utils import timezone


from .validators import validate_blocked_words


class ProductQueryset(models.QuerySet):
  def published(self): # Product.objects.filter().published() & Product.objects.published()
    return self.filter(state=Product.ProductStateOptions.PUBLISH, publish_timestamp__lte=timezone.now())


class ProductManager(models.Manager):
  def get_queryset(self):
    return ProductQueryset(self.models, using=self._db)
  
  def published(self): # Product.objects.published()
    return self.get_queryset().published()
  
class Product(models.Model):
  class ProductStateOptions(models.TextChoices):
    PUBLISH = 'PU', 'Published'
    DRAFT = 'DR', 'Draft'
    PRIVATE = 'PR', 'Private'
    # obj.get_state_display()
    # state=Product.productstateoptions.PUBLISH

  title = models.CharField(max_length=120, validators=[validate_blocked_words]) # unique=True
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

  @property
  def state_is_published(self):
    return self.state == self.ProductStateOptions.PUBLISH
  
  @property
  def is_published(self):
    publish_timestamp = self.publish_timestamp
    return self.state_is_published and publish_timestamp < timezone.now()
  # def is_published(self):
  #   return self.state == self.ProductStateOptions.PUBLISH
