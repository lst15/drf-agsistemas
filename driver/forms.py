from django import forms
from django.core.validators import RegexValidator

class DriverCreateForm(forms.Form):
  name = forms.CharField(
    min_length=4,
    max_length=200,
  )
  phone = forms.CharField(
    min_length=9,
    max_length=11,
    
    validators=[
      RegexValidator(
        regex=r'^(\d{2})\D*(\d{5}|\d{4})\D*(\d{4})$',
        message='Formato de numero invalido.',
        code='invalid_phone'
      )         
    ]    
  )
  license = forms.CharField(
    min_length=10,
    max_length=10
  )