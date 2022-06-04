from cgitb import html
from multiprocessing import context
from django.shortcuts import render
from ProductosApp.models import Productos


def buscar(request):
    try:
        producto = Productos.objects.get(nombre = request.GET['search'])
        context = {'producto': producto}
        return render(request, 'buscar.html', context = context)
    except:
        context = {'errors':'No se encontro el producto'}
        return render(request, 'buscar.html', context = context)

def productos(request):

    nuevo_producto = Productos.objects.create(
        nombre = "dd",
        precio = "3",
        descripcion = 'df',
        stock = '33',
        )

    context = {'nuevo_producto':nuevo_producto}

    return render(request,'productos.html', context = context)










