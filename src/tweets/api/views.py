from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

from tweets.models import Tweet
from .serializers import TweetModelSerializer
from .pagination import StandardResultsPagination
# from rest_framework.response import Response


class TweetCreateAPIView(CreateAPIView):
  serializer_class = TweetModelSerializer
  permission_classes = [IsAuthenticated]

  def perform_create(self, serializer):
    serializer.save(user=self.request.user)


class TweetListAPIView(ListAPIView):
  serializer_class = TweetModelSerializer
  pagination_class = StandardResultsPagination

  def get_queryset(self, *args, **kwargs):
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
