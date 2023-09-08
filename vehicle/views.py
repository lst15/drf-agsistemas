from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import VehicleModel
from .serializers import VehicleSerializer
from .forms import VehicleCreateForm,VehicleUpdateOilForm
from .models import VehicleModel

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

class upateOil(APIView):
  def put(self, request,vehicle_id):
    form = VehicleUpdateOilForm(request.data)
    
    if(form.errors):
      return Response({"error": form.errors}, status=400)

    data = form.cleaned_data

    try:
        vehicle = VehicleModel.objects.get(pk=vehicle_id)
        vehicle.vehicle_oil_change_km = data['oil_change_km']
    except VehicleModel.DoesNotExist:
        return Response({"error": "Vehicle not found"}, status=404)
    
    vehicle.save()

    return Response({
        "success": True,
        "message": "Vehicle updated successfully",
    })

class fetch(APIView):
  def get(self,request,vehicle_id):
    try:
        vehicle = VehicleModel.objects.get(pk=vehicle_id)        
    except VehicleModel.DoesNotExist:
        return Response({"error": "Vehicle not found"}, status=404)
    
    data = {
      "plate":vehicle.vehicle_plate,
      "brand":vehicle.vehicle_brand,
      "model":vehicle.vehicle_model,
      "oil_change_km":vehicle.vehicle_oil_change_km
    }
    
    return Response({"vehicle":data})

class fetchAll(APIView):
  def get(self, request):
    vehicles = VehicleModel.objects.all()
    serializer = VehicleSerializer(vehicles, many=True)

    return Response({
        "success": True,
        "results": serializer.data,
    }, status=200)

class deleteVehicle(APIView):
  def delete(self, request, vehicle_id):
    try:
      vehicle = VehicleModel.objects.get(pk=vehicle_id)
    except VehicleModel.DoesNotExist:
        return Response({"error": "Vehicle not found"}, status=404)

    vehicle.delete()

    return Response({
        "success": True,
        "message": "Driver deleted successfully",
    })