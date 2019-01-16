from django.db import models
from django.contrib.auth.models import User, AbstractUser

from . import global_vars
from django.template.defaultfilters import slugify

# class Permiso(models.Model):
#     id_permiso = models.AutoField(primary_key=True)
#     permiso = models.CharField(max_length=40, unique=True)
#     descripcion = models.TextField(max_length=400)
#
#     def __str__(self):
#         return self.permiso
#
#     class Meta:
#         ordering = ['id_permiso','permiso']
#         verbose_name_plural = "Permisos"
#
# class Rol(models.Model):
#     id_rol = models.AutoField(primary_key=True)
#     rol = models.CharField(max_length=40, unique=True)
#     descripcion = models.TextField(max_length=400)
#     permisos = models.ManyToManyField(Permiso, help_text="Selecciona los permisos de éste Rol")
#
#     def __str__(self):
#         return self.rol
#
#     class Meta:
#         ordering = ['id_rol','rol']
#         verbose_name_plural = "Roles"

class Usuario(AbstractUser):

    # Verificar la conveniencia de este campo (mejor poner un ojito en el template de modo que se vea la contraseña ingresada)
    confirm_password = models.CharField(max_length=60, blank=True, null=True)

    birth_date = models.DateField()

    imagen = models.ImageField(upload_to='usuarios/img/profile', default = global_vars.DEFAULT_USER_IMAGE)

    # No se hace necesario el uso de Identificación
    # tipos_id = (
    #         ('CC', 'Cédula de Ciudadanía'),
    #         ('TI', 'Tarjeta de Identidad'),
    #         ('CE', 'Cédula de Extrangería'),
    #         ('PS', 'Pasaporte'),
    #     )

    #tipo_id = models.CharField(max_length=2, choices=tipos_id, default='CC',
    #                             help_text="Identificador del tipo de identificación",
    #                              )
    #identificacion = models.CharField(max_length=20, help_text="Número identificación"                              )

    def save(self,*args,**kwargs):
        #self.slug = slugify(self.username)#No sé hace esto para dejar de usar el slug en vez de username
        super (Usuario,self).save(*args,**kwargs)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['username']