from django.db import models

# Create your models here.

class BillingItem(models.Model):
  item_name = models.CharField(max_length=120, null=True, blank=True)
  number_1 = models.IntegerField(default=0)
  number_2 = models.IntegerField(default=0)
  total = models.IntegerField(default=0)
  timestamp = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.total