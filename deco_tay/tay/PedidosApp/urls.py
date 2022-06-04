import imp
from django.urls import path
from PedidosApp.views import pedidos

urlpatterns =[
    path('pedidos/', pedidos, name = 'pedidos'),
]