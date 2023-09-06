from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import VehicleModel
from .serializers import VehicleSerializer
from .forms import VehicleCreateForm

class create(APIView):
  def post(self,request):
    form = VehicleCreateForm(request.data)
        
    if(form.errors):
      return Response({"error": form.errors}, status=400)
    
    data = form.cleaned_data
    
    serial = VehicleSerializer(
      VehicleModel.objects.create(
        vehicle_plate=data["plate"],
        vehicle_brand=data["brand"],
        vehicle_model=data["model"],
        vehicle_oil_change_km=data["oil_change_km"]
      )
    )    
    
    return Response({"vehicle": serial.data}, status=201)

