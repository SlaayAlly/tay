from django.db import models

# Create your models here.

class Productos(models.Model):
    nombre = models.TextField(max_length=50)
    precio = models.FloatField()
    descripcion = models.TextField(max_length=200)
    imagen = models.ImageField(upload_to='productos/')
    stock = models.IntegerField()
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'