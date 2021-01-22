from django.shortcuts import render

from django.template import loader

from .models import *

def index(request):
    return render(request, 'main/getName.html')

def formulario(request):
    sd = Sandwich.objects.all()
    ing = Ingrediente.objects.all()

    if request.method == 'POST' and 'add' in request.POST: 
        venta = Venta.objects.get(id=request.POST['venta'])
        cliente = Cliente.objects.get(fk_venta=venta.id)

        cs = CliSan.objects.create(fk_sandwich=request.POST['size'], fk_cliente=cliente.id)

        ingredientes = request.POST.getlist('spice')

        for ing in ingredientes:
            SanIng.objects.create(fk_ingrediente=ing, fk_sandwich=cs.id)

        return render(request, 'main/sandwich.html', {'sd': sd, 'ing': ing, 'cli':cliente.nombre})

    elif request.method == 'POST' and 'confirm' in request.POST: 
        venta = Venta.objects.get(id=request.POST['venta'])
        cliente = Cliente.objects.get(fk_venta=venta.id)

        return render(request, 'main/.html')

    elif request.method == 'POST' and 'cancelar' in request.POST: 
        venta = Venta.objects.filter(id=request.POST['venta'])
        venta.delete()

        return render(request, 'main/.html')

    else:
        venta = Venta.objects.create()

        cliente = Cliente.objects.create(nombre=request.POST['name'])
        cliente.fk_venta = venta

        return render(request, 'main/sandwich.html', {'name': cliente.nombre, 'sd': sd, 'ing': ing, 'v':venta})