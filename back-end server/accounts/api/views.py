from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    ListAPIView
)

from .serializers import ProfileSerializer
from accounts.models import Account


class AllUsersAPIView(ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Account.objects.all()


class RegisterAPIView(CreateAPIView):
    serializer_class = ProfileSerializer
    queryset = Account.objects.all()


class ProfileAPIView(RetrieveAPIView):
    serializer_class = ProfileSerializer
    lookup_url_kwarg = 'id'
    lookup_field = 'id'

    def get_queryset(self, *args, **kwargs):
        queryset = Account.objects.filter(id=self.kwargs['id'])
        return queryset


class ProfileUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def get_queryset(self, *args, **kwargs):
        queryset = Account.objects.filter(id=self.kwargs['id'])
        return queryset


class ProfileDeleteAPIView(DestroyAPIView):
    serializer_class = ProfileSerializer
    lookup_field = 'id'

    def get_queryset(self, *args, **kwargs):
        queryset = Account.objects.filter(id=self.kwargs['id'])
        return queryset
