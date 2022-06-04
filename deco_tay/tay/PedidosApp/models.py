from random import choices
from tkinter import Widget
from django.db import models
from django import forms
# Create your models here.


generos= [
    ('hetero', 'Heterosexual'),
    ('homo', 'Homosexual'),
    ('bi', 'Bisexual'),
    ('ase', 'Asexual'),
    ('pan', 'Pansexual'),
    ]

class Pedidos(models.Model):
    cliente =models.TextField(max_length=30)
    cantidad_de_articulos = models.IntegerField()
    # Pendiente -- articulo = models.CharField(widget =forms.Select(choices=generos) )
    articulo1 = models.TextField(max_length=30)
    articulo2 = models.TextField(max_length=30)
    articulo3 = models.TextField(max_length=30)
    articulo4 = models.TextField(max_length=30)
    observaciones = models.TextField(max_length=1000)



#class formulario(forms.Form):
    #nombre= forms.CharField(max_length=100)
    #apellido= forms.CharField(max_length=100)
    #genero= forms.CharField(label='Seleccione su genero', widget=forms.Select(choices=genero))
    #comentario= forms.CharField(max_length=100)


