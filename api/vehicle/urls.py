from django.urls import path
from .views import create

urlpatterns = [
  path("vehicle", create.as_view(),name="create")
]