from django.urls import path
from .views import create,upateOil,fetch,fetchAll,deleteVehicle

urlpatterns = [
  path("vehicle", create.as_view(),name="create"),
  path('vehicle/<int:vehicle_id>/update_oil', upateOil.as_view(), name='update_oil'),
  path("vehicle/<int:vehicle_id>", fetch.as_view(),name="fetch"),
  path("vehicle/fetch", fetchAll.as_view(),name="fetchAll"),
  path('vehicle/<int:vehicle_id>/delete', deleteVehicle.as_view(), name='delete'),
]