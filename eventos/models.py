from django.db import models

# class Evento(models.Model):
#     id_evento = models.AutoField(primary_key=True, default=1)
#     nombre = models.CharField(max_length=100)
#     descripcion = models.CharField(max_length=450)
#     fecha = models.DateTimeField()
#     edades = (
#         ('T', 'Apta para todo público'),
#         ('7','Recomendada para mayores de 7 años'),
#         ('12', 'Recomendada para mayores de 12 años'),
#         ('15', 'Apta para mayores de 15 años'),
#         ('18', 'Apta para mayores de 18 años'),
#         ('X', 'Apta para mayores de 18 años, con alto contenido sexual'),
#     )
#
#     apto = models.CharField(max_length=2, choices=edades, blank=True, default='T', help_text="Identificador de las edades admitidas de acuerdo a la tematica del Evento")
#
#     def __str__():
#         """
#         String que representa al objeto Evento
#         """
#         return self.nombre
