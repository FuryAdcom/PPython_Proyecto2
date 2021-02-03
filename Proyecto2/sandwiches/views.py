from django.shortcuts import render
from django.template import loader

import datetime

from .models import *

#funciones para agarrar el nombre de la persona
def index(request):
    return render(request, 'main/getName.html')

#funciones que se utilizan para los formularios 
def formulario(request):
    sd = Sandwich.objects.all()
    ing = Ingrediente.objects.all()
    ref = Refresco.objects.all()

    if request.method == 'POST' and 'add' in request.POST: 
        venta = Venta.objects.get(pk=request.POST['venta'])
        cliente = Cliente.objects.get(fk_venta=venta.pk)

        x = Sandwich.objects.get(pk=request.POST['size'])
        cs = CliSan.objects.create(fk_sandwich=x, fk_cliente=cliente)

        ingredientes = request.POST.getlist('spice')

        for ingr in ingredientes:
            x = Ingrediente.objects.get(pk=ingr)
            SanIng.objects.create(fk_ingrediente=x, fk_sandwich=cs)

        cs = cliente.clisan_set.all()
        csid = cs.values_list('id', flat=True)
        ci = SanIng.objects.filter(fk_sandwich__in=list(csid))
        cr = cliente.cliref_set.all()

        monto = 0
        for sand in cs:
            x = Sandwich.objects.get(pk=sand.fk_sandwich.id)

            gen = (ingr for ingr in ci if ingr.fk_sandwich.id == sand.pk)
            for ingr in gen:
                y = Ingrediente.objects.get(pk=ingr.fk_ingrediente.id)
                monto += y.precio

            monto += x.precio
        venta.monto_total = monto
        venta.save()

        return render(request, 'main/sandwich.html', {'sd': sd, 'ing': ing, 'ref':ref, 'cs': cs, 'cr': cr, 'ci': ci, 'venta': venta})

    elif request.method == 'POST' and 'confirm' in request.POST: 
        venta = Venta.objects.get(pk=request.POST['venta'])
        cliente = Cliente.objects.get(fk_venta=venta.pk)

        venta.fecha = datetime.datetime.now()
        venta.save()

        alert = ('success','realizada')

        return render(request, 'main/getName.html', {'alert': alert})

    elif request.method == 'POST' and 'cancelar' in request.POST: 
        venta = Venta.objects.filter(pk=request.POST['venta'])
        venta.delete()

        alert = ('danger','cancelada')

        return render(request, 'main/getName.html', {'alert': alert})

    else:
        venta = Venta.objects.create()

        cliente = Cliente.objects.create(nombre=request.POST['name'], fk_venta=venta)

        return render(request, 'main/sandwich.html', {'name': cliente.nombre, 'ref':ref, 'sd': sd, 'ing': ing, 'venta':venta})

#funciones que se utilizan para los formularios de extras
def extra(request):
    sd = Sandwich.objects.all()
    ing = Ingrediente.objects.all()
    ref = Refresco.objects.all()
    
    venta = Venta.objects.get(pk=request.POST['venta'])
    cliente = Cliente.objects.get(fk_venta=venta.pk)
    cs = cliente.clisan_set.all()
    csid = cs.values_list('id', flat=True)
    ci = SanIng.objects.filter(fk_sandwich__in=list(csid))

    refrescos = request.POST.getlist('refres')

    monto = 0

    for re in refrescos:
        r = Refresco.objects.get(pk=re)
        cant = request.POST['refcant'+str(r.pk)]

        for i in range(int(cant)):
            CliRef.objects.create(fk_cliente=cliente,fk_refresco = r)
            monto += r.precio

    venta.monto_total += monto
    venta.save()

    cr = cliente.cliref_set.all()

    return render(request, 'main/sandwich.html', {'ref': ref, 'sd': sd, 'ing': ing, 'cs': cs, 'cr': cr, 'ci': ci, 'venta':venta})
