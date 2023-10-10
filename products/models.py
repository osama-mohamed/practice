from django.db import models


from .validators import validate_blocked_words


PIBLISH_STATE_CHOICES = (
  # ('DB value', 'user display value')
  ('pu', 'Published'),
  ('dr', 'Draft'),
  ('pr', 'Private'),
)

class Product(models.Model):
  title = models.CharField(max_length=120, validators=[validate_blocked_words])
  state = models.CharField(max_length=2, default='dr',
                           choices=PIBLISH_STATE_CHOICES)
  description = models.TextField(null=True)
  price = models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self):
    return self.title

  def save(self, *args, **kwargs):
    validate_blocked_words(self.title)
    super().save(*args, **kwargs)

  @property
  def is_published(self):
    return self.state == 'pu'
