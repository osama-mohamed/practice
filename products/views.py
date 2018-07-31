from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .models import Product
from .forms import ProductForm, RawProductForm

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)


def product_update_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)


def product_delete_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    if request.method == 'POST':
        obj.delete()
        return redirect('../../')
    context = {
       'object' : obj
    }
    return render(request, 'products/product_delete.html', context)


def dynamic_product_detail_view(request, my_id):
    try:
        obj = Product.objects.get(id=my_id)
    except Product.DoesNotExist:
        raise Http404
    context = {
       'object' : obj
    }
    return render(request, 'products/product_detail.html', context)


def product_list_view(request):
    qs = Product.objects.all()
    context = {
       'object_list' : qs
    }
    return render(request, 'products/product_list.html', context)