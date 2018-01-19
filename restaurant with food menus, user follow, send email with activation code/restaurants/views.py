from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.db.models import Q
from .models import RestaurantLocation
from .forms import RestaurantCreateForm, RestaurantLocationCreateForm


class RestaurantListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return RestaurantLocation.objects.filter(user=self.request.user)
        # slug = self.kwargs.get('slug')
        # if slug:
        #     queryset = RestaurantLocation.objects.filter(
        #         Q(category__iexact=slug) |
        #         Q(category__icontains=slug)
        #     )
        # else:
        #     queryset = RestaurantLocation.objects.all()
        # return queryset


class RestaurantDetailView(LoginRequiredMixin, DetailView):
    # queryset = RestaurantLocation.objects.all()
    def get_queryset(self):
        return RestaurantLocation.objects.filter(user=self.request.user)

    # def get_object(self, *args, **kwargs):
    #     rest_id = self.kwargs.get('rest_id')
    #     obj = get_object_or_404(RestaurantLocation, id=rest_id)
    #     return obj


class RestaurantCreateView(LoginRequiredMixin, CreateView):
    form_class = RestaurantLocationCreateForm
    template_name = 'form.html'
    # success_url = ''
    login_url = '/login/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super(RestaurantCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Restaurant'
        return context


class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
    form_class = RestaurantLocationCreateForm
    template_name = 'restaurants/detail-update.html'
    # template_name = 'form.html'
    # success_url = ''
    login_url = '/login/'

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantUpdateView, self).get_context_data(*args, **kwargs)
        # context['title'] = 'Update Restaurant'
        name = self.get_object().name
        # context['title'] = f'Update Restaurant : {name}'
        context['title'] = 'Update Restaurant : {}'.format(name)
        return context

    def get_queryset(self):
        return RestaurantLocation.objects.filter(user=self.request.user)

# class HomeView(TemplateView):
#     template_name = 'home.html'
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(HomeView, self).get_context_data(*args, **kwargs)
#         return context
