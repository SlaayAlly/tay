# Generated by Django 4.0.4 on 2022-06-04 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PedidosApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedidos',
            old_name='articulo',
            new_name='articulo1',
        ),
    ]
