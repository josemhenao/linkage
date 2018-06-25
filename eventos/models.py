from django.db import models
from lugares.models import Lugar
from usuarios.models import Usuario

class Evento(models.Model):
    id_evento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=450)
    fecha = models.DateTimeField()
    lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE)
    imagen = models.ImageField(null=True, blank=True)

    edades = (
        ('T', 'Apto para todo público'),
        ('7','Recomendada para mayores de 7 años'),
        ('12', 'Recomendada para mayores de 12 años'),
        ('15', 'Apto para mayores de 15 años'),
        ('18', 'Apto para mayores de 18 años'),
        ('X', 'Apto para mayores de 18 años, con alto contenido sexual'),
    )
    apto = models.CharField(max_length=2, choices=edades, blank=True, default='T', help_text="Identificador de las edades admitidas de acuerdo a la tematica del Evento")

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Ticket (models.Model):
    id_ticket = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_evento = models.ForeignKey(Evento, on_delete=models.CASCADE)

    class Meta:
        ordering = ["id_ticket"]

    def __str__(self):
        return "Ticket Nº. "+str(self.id_ticket)