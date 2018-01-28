from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


from .models import Product, Category


class AllProductsListView(ListView):
    queryset = Product.objects.all().order_by('-id')
    template_name = 'products/all_products.html'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(AllProductsListView, self).get_context_data(**kwargs)

        qs = Product.objects.all().order_by('-id')
        paginator = Paginator(qs, self.paginate_by)
        page_request = 'page'
        page = self.request.GET.get(page_request)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
        context['objects'] = queryset
        context['page_request'] = page_request

        context['title'] = 'All Products'
        return context


class ProductsListView(ListView):
    # queryset = Product.objects.all()
    queryset = ''
    template_name = 'products/product_list.html'

    def get_context_data(self, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)
        context['title'] = 'Home'
        context['latest_products'] = Product.objects.all().order_by('-id')[:6]  # [start(offset):stop(limit):step]
        context['recommended'] = Product.objects.all().order_by('number_of_sales')[:3]
        context['recommended_2'] = Product.objects.all().order_by('number_of_sales')[3:6]
        context['categories'] = Category.objects.all().order_by('category')
        context['active_slider'] = Product.objects.filter(slider=True)[:1]
        context['non_active_slider_1'] = Product.objects.filter(slider=True)[1:2]
        context['non_active_slider_2'] = Product.objects.filter(slider=True)[2:3]
        return context

    def post(self, request):
        minimum = self.request.POST.get('minimum')
        maximum = self.request.POST.get('maximum')
        queryset = None
        if not minimum == '' and not maximum == '':
            queryset = Product.objects.filter(price__range=(minimum, maximum))
        else:
            return redirect('products:list')
        context = {
            'products': queryset,
            'categories': Category.objects.all().order_by('category'),
            'title': 'Price Range',
        }
        return render(request, 'products/categories.html', context)


class ProductDetailView(DetailView):
    template_name = 'products/product_detail.html'

    def get_object(self):
        slug = self.kwargs['slug']
        return get_object_or_404(Product, slug=slug, publish=True)

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['recommended'] = Product.objects.all().order_by('number_of_sales')[:3]
        context['categories'] = Category.objects.all().order_by('category')
        return context


class CategoryListView(ListView):
    queryset = ''
    template_name = 'products/categories.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['title'] = 'Category'
        context['categories'] = Category.objects.all().order_by('category')
        context['products'] = Product.objects.filter(category__category=self.kwargs['category'])
        context['current_category'] = self.kwargs['category']
        return context






# for remember
# class List(ListView):
#     def get_queryset(self):
#         return Product.objects.filter(user=self.request.user)
