"""ProyectoSITU URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, reverse
from django.urls import include
from appSITUweb.views import *


urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('pasajeros/', pasajeros, name='pasajeros'),
    path('pasajerosEdit/<id>', pasajerosEdit, name='pasajerosEdit'),
    path('pasajerosNuevo/', pasajerosNuevo, name='pasajerosNuevo'),
    path('pasajerosEliminar/<id>', pasajerosEliminar, name='pasajerosEliminar'),
    path('buses/', buses, name='buses'),
    path('busesEdit/<id>', busesEdit, name='busesEdit'),
    path('busesEliminar/<id>', busesEliminar, name='busesEliminar'),
    path('busesCrear/', busesCrear, name='busesCrear'),
    path('modelado/', modelado_view, name='modelado_view'),
    path('conductor/', conductor, name='conductor'),
    path('conductorEdit/<id>', conductorEdit, name='conductorEdit'),
    path('conductorNuevo/', conductorNuevo, name='conductorNuevo'),
    path('conductorEliminar/<id>', conductorEliminar, name='conductorEliminar'),
    path('tarjeta/', tarjeta, name='tarjeta'),
    path('tarjetaEdit/<id>', tarjetaEdit, name='tarjetaEdit'),
    path('tarjetaNuevo/', tarjetaNuevo, name='tarjetaNuevo'),
    path('tarjetaEliminar/<id>', tarjetaEliminar, name='tarjetaEliminar'),
]
