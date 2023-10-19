from django.views.generic import View, ListView, DetailView
from django.views.generic.list import MultipleObjectMixin
from django.shortcuts import render

from .models import Product, DigitalProduct
from .mixins import ProductTemplateMixin, QuerysetModelMixin


class DigitalProductListView(ProductTemplateMixin, ListView):
  model = DigitalProduct

  def get_title(self):
    return 'Digital Products'



class ProductListView(MultipleObjectMixin, View):
  queryset = Product.objects.filter(pk__gte=0)
  
  def get(self, request, *args, **kwargs):
    self.object_list = self.get_queryset()
    context = self.get_context_data()
    app_label = self.object_list.model._meta.app_label
    model_name = self.object_list.model._meta.model_name
    template = f'{app_label}/{model_name}_list.html'
    return render(request, template, context)



class ProductDetailView(ProductTemplateMixin, DetailView):
  model = Product
  template_name = 'products/product_detail.html'

  def get_title(self):
    return self.get_object().title
