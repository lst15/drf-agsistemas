from django import forms

class ControlCreateForm(forms.Form):
  vehicle_id = forms.IntegerField()
  driver_id = forms.IntegerField()
  departure_date = forms.DateField()
  departure_time = forms.TimeField()
  departure_km = forms.IntegerField(min_value=0)
  destination = forms.CharField(max_length=200)
  return_date = forms.DateField()
  return_time = forms.TimeField()
  return_km =  forms.IntegerField(min_value=0)  
