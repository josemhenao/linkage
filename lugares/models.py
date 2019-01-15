from django.db import models
from django.template.defaultfilters import slugify
from usuarios.models import Usuario
from main.models import Imagen
from .global_vars import DEFAULT_LUGAR_IMAGE


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=60, help_text="Nombre la categoría", unique=True)
    descripcion = models.CharField(max_length=400, help_text="Descripción de la categoría")

    class Meta:
        verbose_name = 'Categoria'
        ordering = ['id_categoria']

    def __str__(self):
        return self.categoria


class Lugar(models.Model):
    id_lugar = models.AutoField("Id_lugar", primary_key=True)

    slug = models.SlugField()

    nombre = models.CharField("Nombre", max_length=60,
                              help_text="Nombre del Lugar"
                              )
    descripcion = models.TextField(max_length=400, null=True, blank=True,
                                   help_text="Descripción del Lugar"
                                   )
    categoria = models.ManyToManyField(Categoria,
                                       verbose_name="Lista of categorias", null=True, blank=True
                                       )

    capacidad = models.IntegerField(
        help_text="Número de personas que caben en el Lugar"
    )

    direccion = models.CharField(max_length=150, null=True, blank=True,
                                 help_text="Dirección del Lugar"
                                 )
    ciudad = models.CharField(max_length=60, null=True, blank=True,
                              help_text="Ciudad donde se encuentra el Lugar"
                              )
    admin = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)

    img_ppal = models.ImageField(upload_to='lugares/img/lugar', null=True, blank=True,
                                 help_text="Imagen principal del Lugar",
                                 default=DEFAULT_LUGAR_IMAGE
                                 )
    imagenes = models.ManyToManyField(to=Imagen, verbose_name="Lista de imagenes", null=True, blank=True)
    # Verificar la importancia de esto (ver si es mejor reescalar la imagen ppal)
    # img_slide = models.ImageField(upload_to='lugares/img/lugar', null=True, blank=True,
    #                               help_text="Imagen de un tamaño 1000 x 330 px, para mostrar en el slide de la"
    #                                         " sección Lugares")

    # Revisar la mejor manera almacenar las imagenes de modo que sea 'n' numero de imagenes
    #img_1 = models.ImageField(upload_to='lugares/img/lugar', null=True, blank=True)
    #img_2 = models.ImageField(upload_to='lugares/img/lugar', null=True, blank=True)
    #img_3 = models.ImageField(upload_to='lugares/img/lugar', null=True, blank=True)

    class Meta:
        verbose_name = 'Lugar'
        verbose_name_plural = "Lugares"
        ordering = ['id_lugar', 'nombre']

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Lugar, self).save(*args, **kwargs)
