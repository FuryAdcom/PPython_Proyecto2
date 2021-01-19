from django.contrib import admin

from .models import *

class VentaAdmin(admin.ModelAdmin):
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