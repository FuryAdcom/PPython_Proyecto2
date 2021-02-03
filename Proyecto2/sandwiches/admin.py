from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path

import datetime

from .models import *

#clase para agarrar los links relacionas a ventas
class VentaAdmin(admin.ModelAdmin):
    list_display = ('monto_total', 'fecha')
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('all/', self.admin_site.admin_view(self.my_view)),
        ]
        return my_urls + urls

    #funcion que agarra todos los datos de la venta
    def my_view(self, request):
        ing = Ingrediente.objects.all()
        ventas = Venta.objects.all()
        sd = Sandwich.objects.all()

        lista = []

        for venta in ventas:
            cliente = Cliente.objects.get(fk_venta=venta)
            cs = cliente.clisan_set.all()
            csid = cs.values_list('id', flat=True)
            ci = SanIng.objects.filter(fk_sandwich__in=list(csid))

            count = 0
            for s in cs:
                count += 1
                for x in sd:
                    if s.fk_sandwich.id == x.pk:
                        for a in ci:
                            if a.fk_sandwich.id == s.id:
                                for y in ing:
                                    if a.fk_ingrediente.id == y.pk:
                                        lista.append([venta.id, venta.monto_total, venta.fecha, cliente.nombre, count, x.size, y.nombre])

        context = dict(
           # Include common variables for rendering the admin template.
           self.admin_site.each_context(request),
           lista = lista,
           key=1,
        )
        return TemplateResponse(request, "admin/ventas.html", context)

admin.site.register(Venta, VentaAdmin)

admin.site.register(Cliente)

#para registrar los demas modelos en el apartado de admin
class SDAdmin(admin.ModelAdmin):
    list_display = ('size', 'precio',)
admin.site.register(Sandwich, SDAdmin)

#para registrar los demas modelos en el apartado de admin
class IngAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio',)
admin.site.register(Ingrediente, IngAdmin)

admin.site.register(CliSan)

admin.site.register(SanIng)

class RefAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio',)
admin.site.register(Refresco, RefAdmin)

admin.site.register(CliRef)