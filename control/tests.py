from django.test import TestCase
from rest_framework.test import APIClient

class ControlTestCase(TestCase):
  def setUp(self):
    self.client = APIClient()
    self.data = {
        'id':1,
        "driver_id": 1,
        "vehicle_id": 1,

        "departure_date": "2023-08-11",
        "departure_time": "10:30:00.000000",

        "return_date": "2023-08-11",
        "return_time": "12:30:00.000000",

        "departure_km": 150,
        "return_km": 250,
        "destination": "Tupa",
    }
    self.data_driver = {
        'id':1,
        'name': 'Mayara',
        'phone': '14996278264',
        'license': '1234567890',
    }
    self.data_vehicle = {
        'id':1,
        'plate': 'ABC-1234',
        'model': 'Fusca',
        'brand': 'Volkswagen',
        "oil_change_km": 1000,
    }

  def test_control_created(self):
    self.client.post('/api/driver', self.data_driver, format='json')
    self.client.post('/api/vehicle', self.data_vehicle, format='json')

    response = self.client.post('/api/control', self.data, format='json')    
    self.assertEqual(response.status_code, 201)

  def test_control_updated(self):
    created_driver = self.client.post('/api/driver', self.data_driver, format='json')
    created_vehicle = self.client.post('/api/vehicle', self.data_vehicle, format='json')

    self.data["driver"] = created_driver.data["driver"]["id"]
    self.data["vehicle"] = created_vehicle.data["vehicle"]["id"]

    created_control = self.client.post('/api/control', self.data, format='json')

    self.data["departure_km"] = 200
    self.data["return_km"] = 300

    response = self.client.put(
      f'/api/control/{created_control.data["control"]["id"]}/update',
      self.data,
      format='json'
    )

    find_control = self.client.get(
      f'/api/control/{created_control.data["control"]["id"]}',
      format='json'
    )

    self.assertEqual(response.status_code, 200)        

  def test_control_deleted(self):
    created_driver = self.client.post('/api/driver', self.data_driver, format='json')
    created_vehicle = self.client.post('/api/vehicle', self.data_vehicle, format='json')

    self.data["driver"] = created_driver.data["driver"]["id"]
    self.data["vehicle"] = created_vehicle.data["vehicle"]["id"]

    created_control = self.client.post('/api/control', self.data, format='json')

    response = self.client.delete(
        f'/api/control/{created_control.data["control"]["id"]}/delete',
        format='json'
    )
    self.assertEqual(response.status_code, 200)

  def test_control_total_km(self):
    created_driver = self.client.post('/api/driver', self.data_driver, format='json')
    created_vehicle = self.client.post('/api/vehicle', self.data_vehicle, format='json')

    self.data["driver"] = created_driver.data["driver"]["id"]
    self.data["vehicle"] = created_vehicle.data["vehicle"]["id"]

    created_control = self.client.post('/api/control', self.data, format='json')

    response = self.client.get(
      f'/api/control/vehicle/{created_control.data["control"]["vehicle"]}/km',
      format='json'
    )

    self.assertEqual(response.status_code, 200)    

  def test_control_find_control(self):
    created_driver = self.client.post('/api/driver', self.data_driver, format='json')
    created_vehicle = self.client.post('/api/vehicle', self.data_vehicle, format='json')

    self.data["driver"] = created_driver.data["driver"]["id"]
    self.data["vehicle"] = created_vehicle.data["vehicle"]["id"]

    created_control = self.client.post('/api/control', self.data, format='json')

    response = self.client.get(
      f'/api/control/{created_control.data["control"]["id"]}',
      format='json'
    )

    self.assertEqual(response.status_code, 200)

  def test_control_find_control_with_invalid_id(self):
    response = self.client.get(
      f'/api/control/999',
      format='json'
    )

    self.assertEqual(response.status_code, 404)
    self.assertEqual(response.data["error"], "Control not found")

  def test_control_create_with_invalid_driver(self):
    created_vehicle = self.client.post('/api/vehicle', self.data_vehicle, format='json')

    self.data["vehicle"] = created_vehicle.data["vehicle"]["id"]
    self.data["driver"] = 999

    response = self.client.post('/api/control', self.data, format='json')

    self.assertEqual(response.status_code, 404)
    self.assertEqual(response.data["error"], "Driver not found")

  def test_control_create_with_invalid_vehicle(self):
    created_driver = self.client.post('/api/driver', self.data_driver, format='json')

    self.data["driver"] = created_driver.data["driver"]["id"]
    self.data["vehicle"] = 999

    response = self.client.post('/api/control', self.data, format='json')

    self.assertEqual(response.status_code, 404)
    self.assertEqual(response.data["error"], "Vehicle not found")