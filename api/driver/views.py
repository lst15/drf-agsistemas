from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import DriverModel
from .forms import DriverCreateForm
from .serializers import DriverSerializer

class create(APIView):
  def post(self,request):
    form = DriverCreateForm(request.data)

    if(form.errors):
      return Response({"error": form.errors}, status=400)
    
    data = form.cleaned_data
    
    serial = DriverSerializer(
      DriverModel.objects.create(
      driver_name=data['name'],
      driver_phone=data['phone'],
      driver_license=data['license']        
      )
    )
    
    return Response({"driver": serial.data}, status=201)

class update(APIView):
  def put(self, request, driver_id):
    form = DriverCreateForm(request.data)
    
    if(form.errors):
      return Response({"error": form.errors}, status=400)
    
    data = form.cleaned_data
    
    try:
      driver = DriverModel.objects.get(pk=driver_id)
      driver.driver_name = data['name']
      driver.driver_phone = data['phone']
      driver.driver_license = data['license']
    except DriverModel.DoesNotExist:
      return Response({"error": "Driver not found"}, status=404)
    
    driver.save()

    return Response({
        "success": True,
        "message": "Driver updated successfully",
    })

class fetch(APIView):
  def get(self,request,driver_id):
    try:
        driver = DriverModel.objects.get(pk=driver_id)        
    except DriverModel.DoesNotExist:
        return Response({"error": "Driver not found"}, status=404)
    
    data = {
      "name":driver.driver_name,
      "phone":driver.driver_phone,
      "license":driver.driver_license
    }
    
    return Response({"driver":data})

class fetchAll(APIView):
  def get(self, request):
    vehicles = DriverModel.objects.all()
    serializer = DriverSerializer(vehicles, many=True)

    return Response({
        "success": True,
        "results": serializer.data,
    }, status=200)

class deleteDriver(APIView):
  def delete(self,request,driver_id):
    try:
      vehicle = DriverModel.objects.get(pk=driver_id)
    except DriverModel.DoesNotExist:
        return Response({"error": "Driver not found"}, status=404)

    vehicle.delete()

    return Response({
        "success": True,
        "message": "Driver deleted successfully",
    })