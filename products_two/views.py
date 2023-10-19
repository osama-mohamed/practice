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



class ProductDetailView(DetailView):
  model = Product
  template_name = 'products/product_detail.html'


class ProductDetailView(MultipleObjectMixin, View): # https://docs.djangoproject.com/en/4.2/ref/class-based-views/
  queryset = Product.objects.all()
  
  def get(self, request, *args, **kwargs):
    pk = kwargs.get('pk')
    self.object_list = self.get_queryset().filter(pk=pk)
    qs = self.object_list
    if not qs.exists():
      raise Http404('This was not found')
    obj = qs.get()
    context = self.get_context_data()
    context['object'] = obj
    app_label = self.object_list.model._meta.app_label
    model_name = self.object_list.model._meta.model_name
    template = f'{app_label}/{model_name}_detail.html'
    return render(request, template, context)
