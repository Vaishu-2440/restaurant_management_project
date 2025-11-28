from rest_framework.test import APITestCase
from rest_framework import status
from home.models import Restaurant

class RestaurantInfoAPITest(APITestCase) :
    def setup(self) :
        self.restaurant = Restaurant.object.create(
            name = 'Test Restaurant',
            address = '123 Test St',
            phone_number = '9876543210',
            email = 'test@gmail.com'
        )
    def test_get_restaurant_info(self) :
        restaurant = self.client.get('/api/restaurant - info/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertEqual(response.data['name'], self.restaurant.name)
        self.assertEqual(response.data['address'], self.restaurant.address)
