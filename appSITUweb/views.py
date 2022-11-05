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

def conductor(request):
    data = ConductorFormulario()    
    chofer = Conductor.objects.all()
    if request.method == 'POST':
        formulario = ConductorFormulario(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
    return render(request,"conductor.html",{"conductor":chofer, 'form':data})

def conductorNuevo(request):
    chofer = Conductor()
    data = {
        'form': ConductorFormulario(instance=chofer)
    }
    if request.method == 'POST':
        formulario = ConductorFormulario(data=request.POST, instance=chofer, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="conductor")
    return render(request, 'conductorEdit.html', data)

def conductorEdit(request, id):
    chofer = get_object_or_404(Conductor, id = id)
    data = {
        'form' : ConductorFormulario(instance=chofer)
    }
    if request.method == 'POST':
        formulario = ConductorFormulario(data=request.POST, instance=chofer, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="conductor")
    return render(request,'conductorEdit.html',data)

def conductorEliminar(request, id):
    chofer = get_object_or_404(Conductor, id=id)
    if chofer:
        chofer.delete()
    return redirect(to="conductor")

def tarjeta(request):
    data = TarjetaFormulario()    
    card = Tarjeta.objects.all()
    if request.method == 'POST':
        formulario = TarjetaFormulario(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()

    return render(request,"tarjeta.html",{"tarjeta":card, 'form':data})

def tarjetaNuevo(request):
    card = Tarjeta()
    data = {
        'form': TarjetaFormulario(instance=card)
    }
    if request.method == 'POST':
        formulario = TarjetaFormulario(data=request.POST, instance=card, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="tarjeta")
    return render(request, 'tarjetaEdit.html', data)

def tarjetaEdit(request, id):
    card = get_object_or_404(Tarjeta, id = id)
    data = {
        'form' : TarjetaFormulario(instance=card)
    }
    if request.method == 'POST':
        formulario = TarjetaFormulario(data=request.POST, instance=card, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="tarjeta")
    return render(request,'tarjetaEdit.html',data)

def tarjetaEliminar(request, id):
    card = get_object_or_404(Tarjeta, id=id)
    if card:
        card.delete()
    return redirect(to="tarjeta")
