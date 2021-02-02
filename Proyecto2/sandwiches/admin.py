from django.contrib import admin

import datetime

from .models import *

class VentaAdmin(admin.ModelAdmin):
    ing = Ingrediente.objects.all()
    ventas = Venta.objects.all()
    sd = Sandwich.objects.all()

    for venta in ventas:
        cliente = Cliente.objects.get(fk_venta=venta)
        cs = cliente.clisan_set.all()
        csid = cs.values_list('id', flat=True)
        ci = SanIng.objects.filter(fk_sandwich__in=list(csid))

        for s in cs:
            for x in sd:
                if s.fk_sandwich.id == x.pk:
                    for a in ci:
                        if a.fk_sandwich.id == s.id:
                            for y in ing:
                                if a.fk_ingrediente.id == y.pk:
                                    list_display = ('monto_total', 'fecha',)

admin.site.register(Venta, VentaAdmin)

admin.site.register(Cliente)

class SDAdmin(admin.ModelAdmin):
    list_display = ('size', 'precio',)
admin.site.register(Sandwich, SDAdmin)

class IngAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio',)
admin.site.register(Ingrediente, IngAdmin)

admin.site.register(CliSan)

admin.site.register(SanIng)