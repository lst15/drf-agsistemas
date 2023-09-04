from django.db import models

class Vehicle(models.Model):
    vehicle_plate = models.CharField(max_length=10)
    vehicle_brand = models.CharField(max_length=100)
    vehicle_model = models.CharField(max_length=100)
    vehicle_oil_change_km = models.IntegerField()

    class Meta:
        db_table = 'vehicle'
