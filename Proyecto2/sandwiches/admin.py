from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path
from django.contrib.admin import AdminSite

import datetime

from .models import *

class VentaAdmin(admin.ModelAdmin):
    list_display = ('monto_total', 'fecha')
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('all/', self.admin_site.admin_view(self.my_view)),
        ]
        return my_urls + urls

    def my_view(self, request):
        # ...
        context = dict(
           # Include common variables for rendering the admin template.
           self.admin_site.each_context(request),
           # Anything else you want in the context...
           key=1,
        )
        return TemplateResponse(request, "main/ventas.html", context)
    # ing = Ingrediente.objects.all()
    # ventas = Venta.objects.all()
    # sd = Sandwich.objects.all()

    # for venta in ventas:
    #     cliente = Cliente.objects.get(fk_venta=venta)
    #     cs = cliente.clisan_set.all()
    #     csid = cs.values_list('id', flat=True)
    #     ci = SanIng.objects.filter(fk_sandwich__in=list(csid))

    #     for s in cs:
    #         for x in sd:
    #             if s.fk_sandwich.id == x.pk:
    #                 for a in ci:
    #                     if a.fk_sandwich.id == s.id:
    #                         for y in ing:
    #                             if a.fk_ingrediente.id == y.pk:
    #                                 

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