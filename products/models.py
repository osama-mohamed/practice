from django.db import models
from django.utils import timezone


from djviews.db.models import BasePublishModel
from .validators import validate_blocked_words


  
class Product(BasePublishModel):
  title = models.CharField(max_length=120, validators=[validate_blocked_words])
  description = models.TextField(null=True)
  price = models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self):
    return self.title

  def save(self, *args, **kwargs):
    validate_blocked_words(self.title)
    super().save(*args, **kwargs)