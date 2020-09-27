from django.contrib.postgres.aggregates import BitOr
from django.db import models

# Create your models here.
class Productor(models.Model):
    id_productor = models.AutoField(primary_key=True)
    nombre_productor = models.CharField(max_length=100)
    nombre_apellido = models.CharField(max_length=100)
    direccion_productor = models.CharField(max_length=100)
    telefono_productor = models.PositiveIntegerField()
    correo_productor = models.EmailField()

    def __str__(self):
        return "Codigo Productor: "+ str(self.id_productor)+" Nombre: "+self.nombre_productor

class CentroAcopio(models.Model):
    id_centro_acopio = models.AutoField(primary_key=True)
    encargado_centro_acopio = models.CharField(max_length=100)
    direccion_centro_acopio = models.CharField(max_length=100)

    def __str__(self):
        return "Codigo Centro Acopio: "+ str(self.id_centro_acopio)+" Encargado: "+self.encargado_centro_acopio

class Bodega(models.Model):
    id_bodega = models.AutoField(primary_key=True)
    encargado_bodega = models.CharField(max_length=100)
    capacidad_bodega = models.PositiveIntegerField()

    def __str__(self):
        return "Capacidad de bodega: "+str(self.capacidad_bodega)

class Entrega(models.Model):
    id_entrega = models.AutoField(primary_key=True)
    id_productor = models.ForeignKey(Productor, on_delete=models.CASCADE)
    id_centro_acopio = models.ForeignKey(CentroAcopio, on_delete=models.CASCADE)
    id_bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)
    fecha_entrega = models.DateField()
    importe_entrega = models.FloatField()

    def __str__(self):
        return "Fecha entrega "+str(self.fecha_entrega) + " Importe: "+ str(self.importe_entrega)