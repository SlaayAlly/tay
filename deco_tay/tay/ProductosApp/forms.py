from attr import fields
from django import forms
from ProductosApp.models import Productos

class FormularioProducto(forms.ModelsForm):
    class Meta:

        model =Productos
        fields = '__all__'