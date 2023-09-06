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