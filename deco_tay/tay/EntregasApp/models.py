from django.db import models
from django.utils import timezone

# Create your models here.

class Entregas(models.Model):
    cliente = models.TextField(max_length=40)
    cantidad_de_productos_a_entregar = models.PositiveIntegerField()
    direccion = models.TextField(max_length=80)
    casaDepartamento = models.TextField(max_length=20)
    entreCalles1 =models.TextField(max_length=20)
    entreCalles2 =models.TextField(max_length=20)
    fecha = models.DateField(default= timezone.now)
    horario = models.TimeField( auto_now=False, auto_now_add=False)
    observaciones = models.TextField(max_length=1000)

