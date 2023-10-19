from typing import Any
from django.db import models
from django.views.generic import View, ListView, DetailView
from django.views.generic.list import MultipleObjectMixin
from django.shortcuts import render
from django.http import Http404

from .models import Product, DigitalProduct
from .mixins import ProductTemplateMixin, QuerysetModelMixin


class DigitalProductListView(ProductTemplateMixin, ListView):
  model = DigitalProduct

  def get_title(self):
    return 'Digital Products'



class ProductListView(ListView):
  model = Product
  title = 'Products'


# class ProductListView(MultipleObjectMixin, View):
#   queryset = Product.objects.filter(pk__gte=0)
  
#   def get(self, request, *args, **kwargs):
#     self.object_list = self.get_queryset()
#     context = self.get_context_data()
#     app_label = self.object_list.model._meta.app_label
#     model_name = self.object_list.model._meta.model_name
#     template = f'{app_label}/{model_name}_list.html'
#     return render(request, template, context)


class ProductDetailView(DetailView):
  model = Product

  # def get_object(self):
  #   url_kwarg_id = self.kwargs.get('id')
  #   qs = self.get_queryset().filter(id=url_kwarg_id)
  #   if not qs.exists():
  #     raise Http404('Product not found')
  #   return qs.get()

  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(*args, **kwargs)
    return context


# class ProductDetailView(MultipleObjectMixin, View): # https://docs.djangoproject.com/en/4.2/ref/class-based-views/
#   queryset = Product.objects.all()
  
#   def get(self, request, *args, **kwargs):
#     pk = kwargs.get('pk')
#     self.object_list = self.get_queryset().filter(pk=pk)
#     qs = self.object_list
#     if not qs.exists():
#       raise Http404('This was not found')
#     obj = qs.get()
#     context = self.get_context_data()
#     context['object'] = obj
#     app_label = self.object_list.model._meta.app_label
#     model_name = self.object_list.model._meta.model_name
#     template = f'{app_label}/{model_name}_detail.html'
#     return render(request, template, context)
