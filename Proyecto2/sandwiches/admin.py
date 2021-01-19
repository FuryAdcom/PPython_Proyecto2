from django.contrib import admin

from .models import Venta, Cliente, Sandwich, Ingrediente, CliSan, SanIng

admin.site.register(Venta)
admin.site.register(Cliente)
admin.site.register(Sandwich)
admin.site.register(Ingrediente)
admin.site.register(CliSan)
admin.site.register(SanIng)