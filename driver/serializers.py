from rest_framework import serializers
from .models import DriverModel


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverModel
        fields = '__all__'
