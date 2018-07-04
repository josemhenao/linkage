from django.db import models

class Imagen (models.Model):
    image = models.ImageField(upload_to='7')

    CHOICES = (
            ('50x50', 'Tamaño 50 x 50 px'),
            ('400x400', 'Tamaño 400 x 400 px'),
            ('ANY', 'Cualquier tamaño'),
            ('CAR', 'Tamaño 1000 x 330 px, Slide '),
        )

    size = models.CharField(max_length=12, choices=CHOICES, blank=True, default='ANY',
                               help_text="Tamaño de la imagen",
                               )

    def __str__(self):
        return self.image

