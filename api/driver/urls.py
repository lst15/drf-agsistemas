from django.urls import path
from .views import create

urlpatterns = [
  path("driver",create.as_view(),name="create")
]