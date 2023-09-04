from django.db import models
from driver.models import Driver
from vehicle.models import Vehicle

class Control(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    control_departure_date = models.DateField()
    control_departure_time = models.TimeField()
    control_departure_km = models.PositiveIntegerField()
    control_destination = models.CharField(max_length=200)
    control_return_date = models.DateField(null=True, blank=True)
    control_return_time = models.TimeField(null=True, blank=True)
    control_return_km = models.PositiveIntegerField(null=True, blank=True)
    control_distance_traveled = models.PositiveIntegerField(null=True, blank=True)
    
    class Meta:
      db_table = 'control'