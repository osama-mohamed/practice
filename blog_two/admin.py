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
  ]
  readonly_fields = [
    'timestamp',
    'updated',
    'on_the_fly_field',
  ]

  def on_the_fly_field(self, obj, *args, **kwargs):
    return f'{obj.title} => {'Active' if obj.active == True else 'Not active'}'
  
  class Meta:
    model = Post


admin.site.register(Post, PostAdmin)