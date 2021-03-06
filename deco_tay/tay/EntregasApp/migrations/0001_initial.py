# Generated by Django 4.0.4 on 2022-06-04 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entregas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.TextField(max_length=40)),
                ('cantidad_de_productos_a_entregar', models.IntegerField()),
                ('direccion', models.TextField(max_length=80)),
                ('casaDepartamento', models.TextField(max_length=20)),
                ('entreCalles1', models.TextField(max_length=20)),
                ('entreCalles2', models.TextField(max_length=20)),
                ('horario', models.TextField(max_length=30)),
                ('observaciones', models.TextField(max_length=1000)),
            ],
        ),
    ]
