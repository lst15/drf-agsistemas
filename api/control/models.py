from django.db import models
from driver.models import DriverModel
from vehicle.models import VehicleModel

class ControlModel(models.Model):
    vehicle = models.ForeignKey(VehicleModel, on_delete=models.CASCADE)
    driver = models.ForeignKey(DriverModel, on_delete=models.CASCADE)
    control_departure_date = models.DateField()
    control_departure_time = models.TimeField()
    control_departure_km = models.PositiveIntegerField()
    control_destination = models.CharField(max_length=200)
    control_return_date = models.DateField(null=True, blank=True)
    control_return_time = models.TimeField(null=True, blank=True)
    control_return_km = models.PositiveIntegerField(null=True, blank=True)
    control_distance_traveled = models.PositiveIntegerField(null=True, blank=True)
    
    class Meta:
      ordering = ['-control_departure_date']
      db_table = 'control'

    def save(self, *args, **kwargs):
      if self.control_return_km:
          self.control_distance_traveled = int(self.control_return_km) - int(self.control_departure_km)

      super(ControlModel, self).save(*args, **kwargs)  