from django.urls import path
from .views import create,update,delete,fetch,fetchAll,vehicleKmControl

urlpatterns = [
  path("control",create.as_view(), name="create"),
  path("control/<int:control_id>",update.as_view(),name="update"),
  path("control/<int:control_id>/delete",delete.as_view(),name="delete"),
  path("control/<int:control_id>/fetch",fetch.as_view(),name="fetch"),
  path("control/fetch",fetchAll.as_view(),name="fetchAll"),
  path("control/vehicle/<int:vehicle_id>/km",vehicleKmControl.as_view(),name="get vehicle km control")
]