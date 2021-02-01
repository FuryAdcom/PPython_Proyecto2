from django.db import models

class Venta(models.Model):
    monto_total = models.FloatField(null=True)
    fecha = models.DateTimeField('fecha de venta', null=True)

class Cliente(models.Model):
    #cedula = models.IntegerField(primary_key=True, max_length=15) Si se coloca cédula, habría que modificar los modelos para identificar el mismo cliente.
    nombre = models.CharField(max_length=80)
    fk_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Sandwich(models.Model):
    size = models.CharField(max_length=12)
    precio = models.FloatField()

# Las m-m son para no tener que hardcodear en la aplicación los precios y tener los tipos con sus montos almacenados en la base, solo necesitando linkear sus respectivas foráneas.
class CliSan(models.Model):
    fk_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fk_sandwich = models.ForeignKey(Sandwich, on_delete=models.CASCADE)

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=15)
    precio = models.FloatField()

# Las m-m son para no tener que hardcodear en la aplicación los precios y tener los tipos con sus montos almacenados en la base, solo necesitando linkear sus respectivas foráneas.
class SanIng(models.Model):
    fk_sandwich = models.ForeignKey(CliSan, on_delete=models.CASCADE)
    fk_ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)