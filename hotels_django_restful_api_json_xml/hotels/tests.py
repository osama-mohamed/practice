from django.test import TestCase, Client

from .models import Provider, Hotel

# Create your tests here.
c = Client()

class ResponseTestCase(TestCase):
  def test_home(self):
    response = c.get('http://127.0.0.1:8000/api/hotels/')
    self.assertEqual(response.status_code, 200)


class ProviderTestCase(TestCase):
  def setUp(self):
    self.provider_a = Provider.objects.create(provider='A')
    self.provider_b = Provider.objects.create(provider='B')
    self.providers_count = Provider.objects.all().count()

  def test_providers_count(self):
    qs = Provider.objects.all().count()
    self.assertEqual(qs, self.providers_count)

class HotelTestCase(TestCase):
  def setUp(self):
    self.provider_a = Provider.objects.create(provider='A')
    self.provider_b = Provider.objects.create(provider='B')
    self.hotel_a = Hotel.objects.create(
      provider=self.provider_a,
      name='Hotel number 1',
      rate=5,
      fare=3000,
      room_amenities='Air conditioning, Lake view, Flat-screen TV',
      city=111,
      adults=2
    )
    self.hotel_b = Hotel.objects.create(
      provider=self.provider_a,
      name='Hotel number 2',
      rate=3,
      fare=1000,
      room_amenities='Air conditioning, Lake view, Flat-screen TV',
      city=222,
      adults=3
    )
    self.hotel_c = Hotel.objects.create(
      provider=self.provider_b,
      name='Hotel number 3',
      rate=3,
      fare=1000,
      room_amenities='Air conditioning, Lake view, Flat-screen TV',
      city=333,
      adults=3
    )
    self.hotels_count = Hotel.objects.all().count()
    self.hotels_provider_a_count = Hotel.objects.filter(provider=self.provider_a).count()
    self.hotels_provider_b_count = Hotel.objects.filter(provider=self.provider_b).count()
    self.providers_count = Provider.objects.all().count()
    self.special_number = 1

  def test_hotels_count(self):
    qs = Hotel.objects.all()
    self.assertEqual(qs.count(), self.hotels_count)
  
  def test_hotels_rate5_count(self):
    qs = Hotel.objects.filter(rate=5)
    self.assertEqual(qs.count(), self.special_number)
  
  def test_hotels_adult2_count(self):
    qs = Hotel.objects.filter(adults=2)
    self.assertEqual(qs.count(), self.special_number)
  
  def test_hotels_city111_count(self):
    qs = Hotel.objects.filter(city=111)
    self.assertEqual(qs.count(), self.special_number)

  def test_hotels_name(self):
    qs = Hotel.objects.all()
    for index in range(self.hotels_count):
      qs.values_list("name", flat=True)[index]
      self.assertEqual(qs.values_list("name", flat=True)[index], f'Hotel number {index+1}')
    self.assertEqual(qs.count(), self.hotels_count)

  def test_hotel_provider_a_count(self):
    qs = Hotel.objects.filter(provider=self.provider_a)
    self.assertEqual(qs.count(), self.hotels_provider_a_count)
  
  def test_hotel_provider_b_count(self):
    qs = Hotel.objects.filter(provider=self.provider_b)
    self.assertEqual(qs.count(), self.hotels_provider_b_count)

  