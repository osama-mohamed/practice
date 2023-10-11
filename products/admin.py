from django.contrib import admin

from .models import Product
# Register your models here.



class ProductAdmin(admin.ModelAdmin):
  list_display = [field.name for field in Product._meta.get_fields()]
  fields = [field.name for field in Product._meta.get_fields() if field.name not in ['id']]
  readonly_fields = ['timestamp', 'updated']
  list_display_links = [field.name for field in Product._meta.get_fields() if field.name in ['id', 'title']]
  list_editable = ['state', 'price']
  class Meta:
    model = Product

admin.site.register(Product, ProductAdmin)