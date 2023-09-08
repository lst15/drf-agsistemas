from django.urls import path
from .views import create,update,fetch,fetchAll,deleteDriver

urlpatterns = [
  path("driver",create.as_view(),name="create"),
  path('driver/<int:driver_id>/update', update.as_view(), name='update_driver'),
  path('driver/<int:driver_id>', fetch.as_view(), name='fetch_driver'),
  path("driver/fetch", fetchAll.as_view(),name="fetchAll"),
  path('driver/<int:driver_id>/delete', deleteDriver.as_view(), name='delete'),
]