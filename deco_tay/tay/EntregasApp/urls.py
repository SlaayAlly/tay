import imp
from django.urls import path

from EntregasApp.views import entregas

urlpatterns =[
    path('',entregas, name = 'entregas'),
]