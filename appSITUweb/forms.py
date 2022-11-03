from django import forms
from .models import *

class PasajeroFormulario(forms.ModelForm):
	class Meta:
		model = Pasajero
		fields=["cedula","nombre","apellido", "email","imagen"] 
		#fields = '__all__'

class BusFormulario(forms.ModelForm):
	class Meta:
		model = Bus
		fields=["placa","cooperativa","numero"] 
		#fields = '__all__'