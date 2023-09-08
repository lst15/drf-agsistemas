from django.test import TestCase
from rest_framework.test import APIClient


class DriverTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.data = {
            'id':1,
            'name': 'Geovana',
            'phone': '14996278264',
            'license': '1234567890',
        }

    def test_driver_created(self):
        response = self.client.post('/api/driver', self.data, format='json')

        self.assertEqual(response.status_code, 201)

    def test_driver_updated(self):
        self.client.post('/api/driver', self.data, format='json')
        response = self.client.put('/api/driver/1/update', self.data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_driver_deleted(self):
      self.client.post('/api/driver', self.data, format='json')
      response = self.client.delete('/api/driver/1/delete', self.data, format='json')
      self.assertEqual(response.status_code, 200)

    def test_create_driver_with_missing_fields(self):
      response = self.client.post('/api/driver', {}, format='json')
      self.assertEqual(response.status_code, 400)      

    def test_update_driver_with_invalid_id(self):
      response = self.client.put('/api/driver/999/update', self.data, format='json')
      self.assertEqual(response.status_code, 404)
      self.assertEqual(response.data['error'], 'Driver not found')

    def test_delete_driver_with_invalid_id(self):
      response = self.client.delete('/api/driver/999/delete', format='json')
      self.assertEqual(response.status_code, 404)
      self.assertEqual(response.data['error'], 'Driver not found')