from django.db import models

class Lugar(models.Model):
    id_lugar = models.AutoField("Id_lugar",primary_key=True)
    nombre = models.CharField("Nombre", max_length=60)
    descripcion = models.CharField(max_length=400)
    capacidad = models.IntegerField()
    direccion = models.CharField(max_length=150)
    imagen1 = models.ImageField(null=True, blank=True)
    imagen2 = models.ImageField(null=True, blank=True)
    imagen3 = models.ImageField(null=True, blank=True)
    imagen4 = models.ImageField(null=True, blank=True)
    imagen5 = models.ImageField(null=True, blank=True)