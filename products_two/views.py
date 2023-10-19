from django.views.generic import View, ListView, DetailView
from django.views.generic.list import MultipleObjectMixin
from django.shortcuts import render

from .models import Product, DigitalProduct
from .mixins import ProductTemplateMixin, QuerysetModelMixin


class DigitalProductListView(ProductTemplateMixin, ListView):
  model = DigitalProduct

  def get_title(self):
    return 'Digital Products'



class ProductListView(ListView):
  model = Product
  title = 'Products'



class ProductDetailView(ProductTemplateMixin, DetailView):
  model = Product
  template_name = 'products/product_detail.html'

  def get_title(self):
    return self.get_object().title
