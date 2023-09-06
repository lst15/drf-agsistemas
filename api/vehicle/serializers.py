from rest_framework import serializers
from .models import VehicleModel


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleModel
        fields = '__all__'
