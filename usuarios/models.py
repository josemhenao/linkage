from django.db import models
    
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    username = models.CharField(max_length=45, unique=True)
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60, null=True, blank=True)

    tipos_id = (
        ('CC','Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('CE', 'Cédula de Extrangería'),
        ('PS', 'Pasaporte'),
    )

    tipo_id = models.CharField(max_length=2, choices=tipos_id, blank=True, default='T',
                            help_text="Identificador del tipo de identificación")

    identificacion = models.CharField(max_length=20, default=1)



