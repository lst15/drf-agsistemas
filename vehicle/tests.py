from django.test import TestCase
from rest_framework.test import APIClient

class VehicleTestCase(TestCase):
  def setUp(self):
    self.client = APIClient()
    self.data = {
      'id':1,
      'plate': 'YYY-1234',
      'brand': 'Wolkswagen',
      'model': 'Gol',
      'oil_change_km': 100,
    }

  def test_vehicle_created(self):    
    response = self.client.post('/api/vehicle', self.data, format='json')
    self.assertEqual(response.status_code, 201)
    
  def test_vehicle_updated(self):
    self.client.post('/api/vehicle', self.data, format='json')
    response = self.client.put('/api/vehicle/1/update_oil', self.data, format='json')
    self.assertEqual(response.status_code, 200)

  def test_vehicle_deleted(self):
    self.client.post('/api/vehicle', self.data, format='json')    
    response = self.client.delete('/api/vehicle/1/delete', self.data, format='json')    
    self.assertEqual(response.status_code, 200)

  def test_create_vehicle_with_missing_fields(self):
    response = self.client.post('/api/vehicle', {}, format='json')    
    self.assertEqual(response.status_code, 400)

  def test_update_vehicle_with_invalid_id(self):
    response = self.client.put('/api/vehicle/1/update_oil', self.data, format='json')    
    self.assertEqual(response.status_code, 404)
    self.assertEqual(response.data['error'], 'Vehicle not found')

  def test_delete_vehicle_with_invalid_id(self):
    response = self.client.delete('/api/vehicle/1/delete', format='json')
    self.assertEqual(response.status_code, 404)
    self.assertEqual(response.data['error'], 'Vehicle not found')    
        
