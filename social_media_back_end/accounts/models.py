from django.db import models
from django.conf import settings
from django.db.models.signals import post_save

User = settings.AUTH_USER_MODEL


class Account(models.Model):
  user = models.OneToOneField(User, null=True)
  gender = models.CharField(max_length=6, null=True)
  activation_key = models.CharField(max_length=120, blank=True, null=True)
  activated = models.BooleanField(default=False)
  added = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.user.username


# def post_save_user_receiver(sender, instance, created, *args, **kwargs):
#   if created:
#     is_created = Account.objects.get_or_create(
#       user=instance
#     )

# post_save.connect(post_save_user_receiver, sender=User)