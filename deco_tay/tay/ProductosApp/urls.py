from django.urls import path
from ProductosApp.views import buscar
from ProductosApp.views import productos

urlpatterns =[
    path('buscar/', buscar, name = 'products'),
    path('prod/',productos, name = 'productos'),
]