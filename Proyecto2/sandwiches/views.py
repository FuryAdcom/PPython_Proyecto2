from django.shortcuts import render

from django.template import loader

from .models import *

def index(request):
    return render(request, 'main/getName.html')

def formulario(request):
    sd = Sandwich.objects.all()
    ing = Ingrediente.objects.all()

    if request.method == 'POST' and 'add' in request.POST: 
        venta = request.POST['venta']
        cliente = Cliente.objects.get(fk_venta=venta.id)

        return render(request, 'main/sandwich.html', {'sd': sd, 'ing': ing})

    elif request.method == 'POST' and 'confirm' in request.POST: 
        venta = request.POST['venta']
        cliente = Cliente.objects.get(fk_venta=venta.id)

        return render(request, 'main/.html')

    else:
        venta = Venta.objects.create()

        cliente = Cliente.objects.create(nombre=request.POST['name'], fk_venta=venta.id)

        return render(request, 'main/sandwich.html', {'name': cliente.nombre, 'sd': sd, 'ing': ing, 'v':venta})