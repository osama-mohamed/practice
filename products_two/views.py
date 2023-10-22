from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db import models
from django.forms.models import BaseModelForm
from django.views.generic import View, ListView, DetailView, RedirectView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin, ModelFormMixin
from django.views.generic.list import MultipleObjectMixin
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator


from .models import Product, DigitalProduct
from .mixins import ProductTemplateMixin, QuerysetModelMixin
from .forms import ProductModelForm


class ProductIDRedirectView(RedirectView):

  def get_redirect_url(self, *args, **kwargs):
    pk = self.kwargs.get('pk')
    obj = get_object_or_404(Product, pk=pk)
    return reverse('products_two:detail', kwargs={'slug': obj.slug})
  

class ProductRedirectView(RedirectView):

  def get_redirect_url(self, *args, **kwargs):
    slug = self.kwargs.get('slug')
    # print(self.request.path, self.request.build_absolute_uri())
    return reverse('products_two:detail', kwargs={'slug': slug})
  

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

class MyProductDetailView(LoginRequiredMixin, DetailView):
  model = Product

  # @method_decorator(login_required)
  # def dispatch(self, *args, **kwargs):
  #   return super().dispatch(*args, **kwargs)


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



class ProductCreateView(LoginRequiredMixin, CreateView):
  form_class = ProductModelForm
  template_name = 'products_two/forms.html'
  # success_url = '/products_two/'

  def form_valid(self, form):
    obj = form.save(commit=False)
    obj.user = self.request.user
    obj.save()
    return super().form_valid(form)
  
  # def form_invalid(self, form):
  #   return super().form_invalid(form)


class ProductBaseFormView(LoginRequiredMixin, ModelFormMixin, View):
  form_class = ProductModelForm
  template_name = 'products_two/forms.html'

  # def get_initial(self):
  #   return {'title': 'This is my title'}

  def get(self, request, *args, **kwargs):
    form = self.get_form()
    context = {'form': form}
    return render(request, self.template_name, context)
  
  def post(self, request, *args, **kwargs):
    form = self.get_form()
    if form.is_valid():
      return self.form_valid(form)
    return self.form_invalid(form)

  def form_valid(self, form):
    form.instance.user = self.request.user
    # obj = form.save(commit=False)
    # obj.user = self.request.user
    # obj.save()
    return super().form_valid(form)
  
  def form_invalid(self, form):
    return super().form_invalid(form)
  


def product_update_view(request, slug, *args, **kwargs):
  obj = get_object_or_404(Product, slug=slug)
  form = ProductModelForm(request.POST or None, instance=obj)
  if form.is_valid():
    form.save()
    form = ProductModelForm()
  context = {
    'object': obj,
    'form': form
    }
  return render(request, 'products_two/forms.html', context)



class ProductUpdateView(LoginRequiredMixin, UpdateView):
  form_class = ProductModelForm
  # template_name = 'products_two/forms.html'
  # template_name = 'products_two/product_detail.html'
  template_name_suffix = '_detail'
  # model = Product

  def get_queryset(self):
    return Product.objects.filter(user=self.request.user)
  
  # def get_success_url(self):
  #   return self.object.get_update_url()

  # def form_valid(self, form):
  #   form.instance.user = self.request.user
  #   return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
  template_name = 'products_two/forms_delete.html'
  model = Product
  success_url = reverse_lazy('products_two:list')