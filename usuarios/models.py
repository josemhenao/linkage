from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from passlib.hash import sha256_crypt


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
    birth_date = models.DateField(null=True, blank=True)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, blank=True, null=True)
    imagen = models.ImageField(null=True, blank=True, upload_to='static/img/profile')
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
    #slug = models.SlugField(max_length=40)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        print("Entra a Save Usuario")
        self.slug = slugify(self.username)
        super(Usuario, self).save(*args, **kwargs)

    def verify_pasword(self, raw_password):
        print("entra en verify_password del Modelo")
        equals = sha256_crypt.verify(raw_password, hash)
        print ("self_pass: "+self.password)
        print("equals: "+ equals)
        return equals

