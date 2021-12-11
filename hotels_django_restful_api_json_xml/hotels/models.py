from django.db import models

class Provider(models.Model):
  provider = models.CharField(max_length=255, unique=True)
  def __str__(self):
    return self.provider


class Hotel(models.Model):
  provider = models.ForeignKey(Provider, on_delete=models.SET_NULL, null=True, blank=True)
  name = models.CharField(max_length=250)
  rate = models.PositiveIntegerField()
  fare = models.PositiveIntegerField()
  discount = models.IntegerField(default=0, null=True, blank=True)
  room_amenities = models.TextField()
  city = models.CharField(max_length=250)
  adults = models.PositiveIntegerField(null=True, blank=True)
  dateFrom = models.DateField(auto_now_add=True, null=True, blank=True)
  dateTo = models.DateField(auto_now=True, null=True, blank=True)

  class Meta:
    ordering = ['-rate']
  