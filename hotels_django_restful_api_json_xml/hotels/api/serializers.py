from rest_framework.serializers import (
  ModelSerializer,
  SerializerMethodField,
)

from hotels.models import Hotel

class HotelSerializer(ModelSerializer):
  class Meta:
    model = Hotel
    fields = "__all__"


class HotelSearchSerializer(ModelSerializer):
  room_amenities = SerializerMethodField()
  class Meta:
    model = Hotel
    fields = ['name', 'rate', 'fare', 'room_amenities']

  def get_room_amenities(self, obj):
    return obj.room_amenities.split(',')