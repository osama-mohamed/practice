from django.db.models import Q
from rest_framework.generics import (
  CreateAPIView,
  ListAPIView,
  UpdateAPIView,
  DestroyAPIView,
  RetrieveAPIView,
)

from hotels.models import Hotel
from .serializers import(
  HotelSerializer,
  HotelSearchSerializer,
)


class CreateHotelAPIView(CreateAPIView):
  """Creates a new hotel"""
  queryset = Hotel.objects.all()
  serializer_class = HotelSerializer

class ListHotelAPIView(ListAPIView):
  """Lists all hotels from the database"""
  queryset = Hotel.objects.all()
  serializer_class = HotelSerializer

class DetailHotelAPIView(RetrieveAPIView):
  """Detail the hotel where id has been passed through the request"""
  queryset = Hotel.objects.all()
  serializer_class = HotelSerializer
  lookup_field = 'pk'

class UpdateHotelAPIView(UpdateAPIView):
  """Update the hotel where id has been passed through the request"""
  queryset = Hotel.objects.all()
  serializer_class = HotelSerializer

class DeleteHotelAPIView(DestroyAPIView):
  """Deletes a hotel where id has been passed through the request"""
  queryset = Hotel.objects.all()
  serializer_class = HotelSerializer

class ListHotelSearchAPIView(ListAPIView):
  """Search hotels from the database"""
  queryset = Hotel.objects.all()
  serializer_class = HotelSearchSerializer

  def get_queryset(self, *args, **kwargs):
    queryset = Hotel.objects.all()
    query = self.request.GET
    if query.get('dateFrom') and query.get('dateTo') and query.get('city') and query.get('adults'):
      queryset = Hotel.objects.filter(
        Q( dateFrom__gte=query.get('dateFrom')) |
        Q( dateTo__lte=query.get('dateTo')),
        Q( city__exact=query.get('city') ) |
        Q( adults__gte=query.get('adults') )
      ).distinct()
    return queryset