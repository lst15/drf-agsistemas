from django import forms
from django.core.validators import RegexValidator

class VehicleCreateForm(forms.Form):
    plate = forms.CharField(
        min_length=8,
        max_length=8,
        
        validators=[
            RegexValidator(
                regex=r'^[A-Z]{3}-\d{4}$',
                message='Formato de placa inválido. Use o formato AAA-1234.',
                code='invalid_plate'
            )
        ]
    )
    brand = forms.CharField(
      min_length=3,
      max_length=20,
      help_text="Invalid brand"
    )
    model = forms.CharField(
      min_length=3,
      max_length=20,
      help_text="Invalid model"
    )
    oil_change_km = forms.IntegerField(
      help_text="Oil needs to be a number",
      min_value=1
    )
    