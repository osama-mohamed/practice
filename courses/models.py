from django.db import models
from django.urls import reverse

# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=120)

    def get_absolute_url(self):
        return reverse('courses:courses_detail', kwargs={'id': self.id})

    def get_absolute_update_url(self):
        return reverse('courses:courses_update', kwargs={'id': self.id})

    # def get_absolute_delete_url(self):
    #     return reverse('courses:courses_delete', kwargs={'id': self.id})