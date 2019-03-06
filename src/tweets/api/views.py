from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q

from tweets.models import Tweet
from .serializers import TweetModelSerializer
from .pagination import StandardResultsPagination


class TweetCreateAPIView(CreateAPIView):
  serializer_class = TweetModelSerializer
  permission_classes = [IsAuthenticated]

  def perform_create(self, serializer):
    serializer.save(user=self.request.user)


class TweetListAPIView(ListAPIView):
  serializer_class = TweetModelSerializer
  pagination_class = StandardResultsPagination

  def get_serializer_context(self, *args, **kwargs):
    context = super(TweetListAPIView, self).get_serializer_context(*args, **kwargs)
    context['request'] = self.request
    return context

  def get_queryset(self, *args, **kwargs):
    requested_user = self.kwargs.get("username")
    if requested_user:
      qs = Tweet.objects.filter(user__username=requested_user).order_by("-timestamp")
    else:
      im_following = self.request.user.profile.get_following()
      qs = Tweet.objects.filter(
        Q(user__in=im_following) |
        Q(user=self.request.user)
      )
    query = self.request.GET.get("q", None)
    if query is not None:
      qs = qs.filter(
        Q(content__icontains=query) |
        Q(user__username__icontains=query)
      )
    return qs


class RetweetAPIView(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request, pk, format=None):
    tweet_qs = Tweet.objects.filter(pk=pk)
    message = "Not allowed"
    if tweet_qs.exists() and tweet_qs.count() == 1:
      new_tweet = Tweet.objects.retweet(request.user, tweet_qs.first())
      if new_tweet is not None:
        data = TweetModelSerializer(new_tweet, context={'request': request}).data
        return Response(data)
      message = "Cannot retweet the same tweet in 1 day"
    return Response({"message": message}, status=400)


class LikeToggleAPIView(APIView):
  permission_classes = [IsAuthenticated]
  def get(self, request, pk, format=None):
    tweet_qs = Tweet.objects.filter(pk=pk)
    message = "Not allowed"
    if request.user.is_authenticated():
      is_liked = Tweet.objects.like_toggle(request.user, tweet_qs.first())
      return Response({'liked': is_liked})
    return Response({"message": message}, status=400)



class TweetDetailAPIView(ListAPIView):
  serializer_class = TweetModelSerializer
  pagination_class = StandardResultsPagination
  permission_classes = [AllowAny]

  def get_queryset(self, *args, **kwargs):
    tweet_id = self.kwargs.get("pk")
    qs = Tweet.objects.filter(pk=tweet_id)
    if qs.exists() and qs.count() == 1:
      parent_obj = qs.first()
      qs1 = parent_obj.get_children()
      qs = (qs | qs1).distinct().extra(select={"parent_id_null": 'parent_id IS NULL'})
    return qs.order_by("-parent_id_null", '-timestamp')


# class SearchAPIView(ListAPIView):
#   serializer_class = TweetModelSerializer
#   pagination_class = StandardResultsPagination

#   def get_queryset(self, *args, **kwargs):
#     qs = Tweet.objects.all()
#     query = self.request.GET.get("q", None)
#     if query is not None:
#       qs = qs.filter(
#         Q(content__icontains=query) |
#         Q(user__username__icontains=query)
#       )
#     return qs
