from django.contrib.admin.utils import help_text_for_field
from django.db import models

class Permiso (models.Model):
    id_permiso= models.AutoField(primary_key=True)
    permiso = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=400)

    def __str__(self):
        return self.permiso

class Rol (models.Model):
    id_rol = models.AutoField(primary_key=True)
    rol = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=400)
    permisos = models.ManyToManyField(Permiso, help_text="Selecciona los permisos de éste Rol")

    def __str__(self):
        return self.rol

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    username = models.CharField(max_length=45, unique=True, help_text="Nombre único que te identifica en Linkage")
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60, null=True, blank=True)
    imagen = models.ImageField(null=True, blank=True, upload_to='static/img/profile')
    tipos_id = (
        ('CC','Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('CE', 'Cédula de Extrangería'),
        ('PS', 'Pasaporte'),
    )

    tipo_id = models.CharField(max_length=2, choices=tipos_id, blank=True, default='T',
                            help_text="Identificador del tipo de identificación")
    identificacion = models.CharField(max_length=20, default=1, help_text="Número identificación", unique=True)
    fecha_nacimiento = models.DateField(null=True, blank=True, help_text="Formato dd/mm/YYYY ")
    email = models.EmailField(unique=True, help_text="Correo para registrar su cuenta en Linkage")
    password = models.CharField(max_length=200)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, null=True, blank=True    )
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username




