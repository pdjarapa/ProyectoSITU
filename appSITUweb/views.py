from django.shortcuts import render
from .forms import *
from .models import *
from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.

def home_view(request):
    return render(request,"index.html",{})

def pasajeros(request):
    data = PasajeroFormulario()    
    pasajeros = Pasajero.objects.all()
    if request.method == 'POST':
        formulario = PasajeroFormulario(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()

    return render(request,"pasajeros.html",{"pasajeros":pasajeros, 'form':data})

def pasajerosNuevo(request):
    pasajero = Pasajero()
    data = {
        'form': PasajeroFormulario(instance=pasajero)
    }
    if request.method == 'POST':
        formulario = PasajeroFormulario(data=request.POST, instance=pasajero, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="pasajeros")
    return render(request, 'pasajerosEdit.html', data)

def pasajerosEdit(request, id):
    pasajeros = get_object_or_404(Pasajero, id = id)
    data = {
        'form' : PasajeroFormulario(instance=pasajeros)
    }
    if request.method == 'POST':
        formulario = PasajeroFormulario(data=request.POST, instance=pasajeros, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="pasajeros")

    return render(request,'pasajerosEdit.html',data)

def pasajerosEliminar(request, id):
    pasajero = get_object_or_404(Pasajero, id=id)
    if pasajero:
        pasajero.delete()
    return redirect(to="pasajeros")

def modelado_view(request):
    return render(request,"modelado.html",{})

def buses(request):
    data = BusFormulario()    
    buses = Bus.objects.all()
    if request.method == 'POST':
        formulario = BusFormulario(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
    return render(request,"buses.html",{"buses":buses, 'form':data})

def busesCrear(request):
    bus = Bus()
    data = {
        'form': BusFormulario(instance=bus)
    }
    if request.method == 'POST':
        formulario = BusFormulario(data=request.POST, instance=bus, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="buses")
    return render(request, 'busesEdit.html', data)

def busesEdit(request, id):
    buses = get_object_or_404(Bus, id = id)
    data = {
        'form' : BusFormulario(instance=buses)
    }
    if request.method == 'POST':
        formulario = BusFormulario(data=request.POST, instance=buses, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="buses")
    return render(request,'busesEdit.html',data)

def busesEliminar(request, id):
    bus = get_object_or_404(Bus, id=id)
    if bus:
        bus.delete()
    return redirect(to="buses")