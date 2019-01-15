from django.db import models

class Imagen(models.Model):
    id_imagen = models.AutoField("id_imagen", primary_key=True)
    url = models.CharField("Ruta de lamacenamiento estático", max_length=256, blank=True, null=True)
    imagen = models.ImageField(upload_to='generales', null=True, blank=True,
                                 help_text="Imagen adicional para Lugares o eventos"
                                 )