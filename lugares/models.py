from django.db import models
from usuarios.models import Usuario

class Lugar(models.Model):
    id_lugar = models.AutoField("Id_lugar", primary_key=True)
    name = models.CharField("Nombre", max_length=60)
    description = models.TextField(max_length=400, null=True, blank=True)
    capacity = models.IntegerField()
    addres = models.CharField(max_length=150, null=True, blank=True)
    city = models.CharField(max_length=60, null=True, blank=True)
    admin = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    img_ppal = models.ImageField(upload_to='lugares/img/lugares')
    img_slide = models.ImageField(upload_to='lugares/img/lugares', null=True, blank=True)

    #Revisar la mejor manera almacenar las imagenes de modo que sea n numero de imagenes
    img_1 = models.ImageField(upload_to='lugares/img/lugares', null=True, blank=True)
    img_2 = models.ImageField(upload_to='lugares/img/lugares', null=True, blank=True)
    img_3 = models.ImageField(upload_to='lugares/img/lugares', null=True, blank=True)

    def __str__(self):
        return self.nombre
