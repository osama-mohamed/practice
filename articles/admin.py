from django.contrib import admin

from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
  list_display = ['id', 'title', 'slug', 'user', 'timestamp', 'updated']
  list_display_links = ['id', 'title']
  search_fields = ['title', 'content']

admin.site.register(Article, ArticleAdmin)
