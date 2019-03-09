from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
  CreateView,
  DetailView,
  ListView,
  UpdateView,
  DeleteView,
  View,
)
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Tweet
from .forms import TweetModelForm
from .mixins import (
  FormUserNeededMixin,
  UserOwnerMixin,
)


class TweetCreateView(FormUserNeededMixin, CreateView):
  form_class = TweetModelForm
  template_name = 'tweets/create.html'


class TweetDetailView(DetailView):
  # template_name = "tweets/tweet_detail.html"

  def get_object(self):
    pk = self.kwargs.get("pk")
    obj = get_object_or_404(Tweet, pk=pk)
    return obj


class TweetListView(LoginRequiredMixin, ListView):
  # template_name = "tweets/tweet_list.html"

  def get_queryset(self, *args, **kwargs):
    qs = Tweet.objects.all()
    query = self.request.GET.get("q", None)
    if query is not None:
      qs = qs.filter(
        Q(content__icontains=query) |
        Q(user__username__icontains=query)
      )
    return qs
        
  def get_context_data(self, *args, **kwargs):
    context = super(TweetListView, self).get_context_data(*args, **kwargs)
    context['create_form'] = TweetModelForm()
    context['create_url'] = reverse_lazy('tweet:create')
    return context


class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
  form_class = TweetModelForm
  template_name = 'tweets/update.html'
  # queryset = Tweet.objects.all()
  # model = Tweet
 
  def get_queryset(self):
    obj = Tweet.objects.filter(id=self.kwargs.get("pk"))
    return obj
  
  # def get_success_url(self):
  #   # qs = Tweet.objects.filter(id=self.kwargs.get("pk")).first()
  #   # return reverse('tweet:detail', kwargs={'pk': qs.id})
  #   return reverse('tweet:detail', kwargs={'pk': self.object.id})


class TweetDeleteView(LoginRequiredMixin, DeleteView):
  queryset = Tweet.objects.all()
  # template_name = 'tweets/tweet_confirm_delete.html'
  success_url = reverse_lazy('tweet:list')


class RetweetView(View):
  def get(self, request, pk, *args, **kwargs):
    tweet = get_object_or_404(Tweet, pk=pk)
    if request.user.is_authenticated():
      new_tweet = Tweet.objects.retweet(request.user, tweet)
      return redirect('home')
    return HttpResponseRedirect(tweet.get_absolute_url())
