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
    username = models.CharField(max_length=45, unique=True)
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60, null=True, blank=True)
    imagen = models.ImageField(null=True, blank=True)

    tipos_id = (
        ('CC','Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('CE', 'Cédula de Extrangería'),
        ('PS', 'Pasaporte'),
    )

    tipo_id = models.CharField(max_length=2, choices=tipos_id, blank=True, default='T',
                            help_text="Identificador del tipo de identificación")
    identificacion = models.CharField(max_length=20, default=1)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        nombre_completo = self.nombre + " " + self.apellido
        return nombre_completo



