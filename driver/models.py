from django.db import models

class DriverModel(models.Model):
    driver_name = models.CharField(max_length=200)
    driver_phone = models.CharField(max_length=16)
    driver_license = models.CharField(max_length=20)

    class Meta:
        db_table = 'driver'
