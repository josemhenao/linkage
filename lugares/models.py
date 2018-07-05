from django.db import models
from usuarios.models import Usuario

class Lugar(models.Model):
    id_lugar = models.AutoField("Id_lugar", primary_key=True)
    name = models.CharField("Nombre", max_length=60,
                            help_text="Nombre del Lugar"
                            )
    description = models.TextField(max_length=400, null=True, blank=True,
                                   help_text="Descripción del Lugar"
                                   )
    capacity = models.IntegerField(
        help_text="Número de personas que caben en el Lugar"
    )
    addres = models.CharField(max_length=150, null=True, blank=True,
                              help_text="Dirección del Lugar"
                              )
    city = models.CharField(max_length=60, null=True, blank=True,
                            help_text="Ciudad donde se encuentra el Lugar"
                            )
    admin = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    img_ppal = models.ImageField(upload_to='lugares/img/lugares', null=True, blank=True,
                                 help_text="Imagen principal del Lugar"
                                 )
    img_slide = models.ImageField(upload_to='lugares/img/lugares', null=True, blank=True,
                                  help_text="Imagen de un tamaño 1000 x 330 px, para mostrar en el slide de la"
                                            " sección Lugares")

    #Revisar la mejor manera almacenar las imagenes de modo que sea n numero de imagenes
    img_1 = models.ImageField(upload_to='lugares/img/lugares', null=True, blank=True)
    img_2 = models.ImageField(upload_to='lugares/img/lugares', null=True, blank=True)
    img_3 = models.ImageField(upload_to='lugares/img/lugares', null=True, blank=True)

    def __str__(self):
        return self.name
