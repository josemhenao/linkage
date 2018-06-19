from django.db import models

class Usuario(models.Model):
    username = models.CharField(max_length = 30)
    nombre = models.CharField(max_length = 45)
    apellido = models.CharField(max_length = 45)
    tipo_identificacion = models.CharField(max_length = 15)
    identificacion = models.CharField(max_length=15)
    correo = models.EmailField()
    contraseña = models.CharField(max_length=80)
    fecha_nacimiento = models.DateField()
    #rol

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username','nombre','identificacion','correo','fecha_nacimiento']
    

