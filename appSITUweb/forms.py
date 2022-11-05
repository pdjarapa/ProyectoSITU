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

class TarjetaFormulario(forms.ModelForm):
	class Meta:
		model = Tarjeta
		fields=["codigo","monto","idPasajero"] 
		#fields = '__all__'

class ConductorFormulario(forms.ModelForm):
	class Meta:
		model = Conductor
		fields=["cedula","nombre","apellido", "email","licencia","idplaca","imagen"] 
		#fields = '__all__'