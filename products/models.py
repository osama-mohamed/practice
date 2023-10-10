from django.db import models


from .validators import validate_blocked_words


  
class Product(models.Model):
  class ProductStateOptions(models.TextChoices):
    PUBLISH = 'PU', 'Published'
    DRAFT = 'DR', 'Draft'
    PRIVATE = 'PR', 'Private'
    # obj.get_state_display()
    # state=Product.productstateoptions.PUBLISH

  title = models.CharField(max_length=120, validators=[validate_blocked_words])
  state = models.CharField(max_length=2, default=ProductStateOptions.DRAFT,
                           choices=ProductStateOptions.choices)
  description = models.TextField(null=True)
  price = models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self):
    return self.title

  def save(self, *args, **kwargs):
    validate_blocked_words(self.title)
    super().save(*args, **kwargs)

  @property
  def is_published(self):
    return self.state == self.ProductStateOptions.PUBLISH
