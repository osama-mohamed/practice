from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
  fields = [
    'on_the_fly_field',
    'active',
    'publish',
    'publish_date',
    'title',
    'slug',
    'content',
    'author_email',
    'view_count',
    'timestamp',
    'updated',
    'publish_from',
    'publish_from_two',
  ]
  readonly_fields = [
    'timestamp',
    'updated',
    'on_the_fly_field',
    'publish_from',
    'publish_from_two',
  ]

  def on_the_fly_field(self, obj, *args, **kwargs):
    return f'{obj.title} => {'Active' if obj.active == True else 'Not active'}'
  
  def publish_from(self, obj, *args, **kwargs):
    return f'{str(obj.publish_from_time())} ago'
  
  def publish_from_two(self, obj, *args, **kwargs):
    return str(obj.other_publish_time)
  
  class Meta:
    model = Post


admin.site.register(Post, PostAdmin)