from rest_framework import serializers
from .models import ControlModel


class ControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlModel
        fields = '__all__'
