# Generated by Django 4.0.4 on 2022-06-04 16:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('EntregasApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entregas',
            name='horario2',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='entregas',
            name='horario',
            field=models.TimeField(),
        ),
    ]