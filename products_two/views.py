from django.views.generic import View, ListView, DetailView
from django.shortcuts import render

from .models import Product, DigitalProduct
from .mixins import ProductTemplateMixin, QuerysetModelMixin


class DigitalProductListView(ProductTemplateMixin, ListView):
  model = DigitalProduct

  def get_title(self):
    return 'Digital Products'



class ProductListView(QuerysetModelMixin, View):
  queryset = Product.objects.filter(pk__gte=0)
  
  def get(self, request, *args, **kwargs):
    context = self.get_context_data()
    template = self.get_template()
    return render(request, template, context)



class ProductDetailView(ProductTemplateMixin, DetailView):
  model = Product
  template_name = 'products/product_detail.html'

  def get_title(self):
    return self.get_object().title
