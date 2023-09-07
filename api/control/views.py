from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import ControlCreateForm
from vehicle.models import VehicleModel
from driver.models import DriverModel
from .serializers import ControlSerializer
from .models import ControlModel
from vehicle.serializers import VehicleSerializer
from driver.serializers import DriverSerializer
from rest_framework.pagination import PageNumberPagination

class create(APIView):
  def post(self,request):
    form = ControlCreateForm(request.data)
    
    if(form.errors):
      return Response({"error": form.errors}, status=400)

    data = form.cleaned_data
    
    try:
        vehicle = VehicleModel.objects.get(pk=data['vehicle_id'])        
    except VehicleModel.DoesNotExist:
        return Response({"error": "Vehicle not found"}, status=404)

    try:
        driver = DriverModel.objects.get(pk=data['driver_id'])        
    except DriverModel.DoesNotExist:
        return Response({"error": "Driver not found"}, status=404)
    print(data)
    serial = ControlSerializer(
      ControlModel.objects.create(
        vehicle = vehicle,
        driver = driver,
        control_departure_date = data['departure_date'],
        control_departure_time = data['departure_time'],
        control_departure_km = data['departure_km'],
        control_destination = data['destination'],
        control_return_date = data['return_date'],
        control_return_time = data['return_time'],
        control_return_km = data['return_km'],        
      )
    )
    
    return Response({"control": serial.data}, status=201)

class update(APIView):
  def put(self,request,control_id):
    form = ControlCreateForm(request.data)
    
    if(form.errors):
      return Response({"error":form.errors}, status=400)
    
    data = form.cleaned_data
    
    try:
      control = ControlModel.objects.get(pk=control_id)
    except ControlModel.DoesNotExist:
      return Response({"error": "Control not found"},status=404)
    
    try:
        vehicle = VehicleModel.objects.get(pk=data['vehicle_id'])        
    except VehicleModel.DoesNotExist:
        return Response({"error": "Vehicle not found"}, status=404)

    try:
        driver = DriverModel.objects.get(pk=data['driver_id'])        
    except DriverModel.DoesNotExist:
        return Response({"error": "Driver not found"}, status=404)    
    
    control.vehicle = vehicle
    control.driver = driver
    control.control_departure_date = request.data.get("departure_date", control.control_departure_date)
    control.control_departure_time = request.data.get("departure_time", control.control_departure_time)
    control.control_departure_km = request.data.get("departure_km", control.control_departure_km)
    control.control_destination = request.data.get("destination", control.control_destination)
    control.control_return_date = request.data.get("return_date", control.control_return_date)
    control.control_return_time = request.data.get("return_time", control.control_return_time)
    control.control_return_km = request.data.get("return_km", control.control_return_km)    
    
    control.save()
    
    return Response({
        "success": True,
        "message": "Control updated successfully",
    })

class delete(APIView):
  def delete(self,request,control_id):
    try:
      control = ControlModel.objects.get(pk=control_id)
    except ControlModel.DoesNotExist:
      return Response({"error": "Control not found"},status=404)

    control.delete()

    return Response({
        "success": True,
        "message": "Control deleted successfully",
    }, status=200)

class fetch(APIView):
  def get(self,request,control_id):
    try:
      control = ControlModel.objects.get(pk=control_id)
      vehicle = VehicleModel.objects.get(pk=control.vehicle.id)
      driver = DriverModel.objects.get(pk=control.driver.id)
    except ControlModel.DoesNotExist:
      return Response({"error": "Control not found"},status=404)

    serial_control = ControlSerializer(control)
    serial_vehicle = VehicleSerializer(vehicle)
    serial_driver = DriverSerializer(driver)
    
    return Response({
        "success": True,
        "control": serial_control.data,
        "vehicle": serial_vehicle.data,
        "driver": serial_driver.data
    }, status=200)

class fetchAll(APIView):
  def get(self,request):
    paginator = PageNumberPagination()
    controls = ControlModel.objects.all().order_by('-control_departure_date')
    
    paginator.page_size = request.GET.get('page_size', 10)
    search_query = request.GET.get('search', None)
    
    if search_query:
        controls = controls.filter(control_departure_date__icontains=search_query) | controls.filter(control_return_date__icontains=search_query)
    
    result_page = paginator.paginate_queryset(controls, request)
    serializer = ControlSerializer(result_page, many=True)

    return Response({
        "success": True,
        "total_items": paginator.page.paginator.count,
        "total_pages": paginator.page.paginator.num_pages,
        "current_page": paginator.page.number,
        "results": serializer.data,
    }, status=200)

class vehicleKmControl(APIView):
  def get(self, request, vehicle_id):
    try:
      vehicle = VehicleModel.objects.get(pk=vehicle_id)
    except VehicleModel.DoesNotExist:
      return Response({"error": "Vehicle not found"}, status=404)

    controls = ControlModel.objects.filter(vehicle=vehicle_id)
    km_total = sum(control.control_distance_traveled for control in controls)
    km_left = vehicle.vehicle_oil_change_km - km_total

    message = "Vehicle exceeded the km limit" if km_total >= vehicle.vehicle_oil_change_km else "Vehicle is within the km limit"

    return Response({
      "success": True,
      "message": message,
      "oil_change_km": vehicle.vehicle_oil_change_km,
      "km_left": km_left,
      "total_km": km_total
    }, status=200)
