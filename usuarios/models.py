from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from passlib.hash import pbkdf2_sha256


class Permiso(models.Model):
    id_permiso = models.AutoField(primary_key=True)
    permiso = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=400)


    def __str__(self):
        return self.permiso

class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    rol = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=400)
    permisos = models.ManyToManyField(Permiso, help_text="Selecciona los permisos de éste Rol")

    def __str__(self):
        return self.rol



class Usuario(User):
    birth_date = models.DateField()

    tipos_id = (
            ('CC', 'Cédula de Ciudadanía'),
            ('TI', 'Tarjeta de Identidad'),
            ('CE', 'Cédula de Extrangería'),
            ('PS', 'Pasaporte'),
        )

    tipo_id = models.CharField(max_length=2, choices=tipos_id, blank=True, default='T',
                                   help_text="Identificador del tipo de identificación",
                                   )
    identificacion = models.CharField(max_length=20, default=1, help_text="Número identificación",
                                      unique=True)