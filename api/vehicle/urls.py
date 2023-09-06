from django.urls import path
from .views import create,upateOil

urlpatterns = [
  path("vehicle", create.as_view(),name="create"),
  path('vehicle/<int:vehicle_id>/update_oil', upateOil.as_view(), name='update_oil'),
]