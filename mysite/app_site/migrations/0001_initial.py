# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 02:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Insumos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(max_length=45)),
                ('hora_inicio', models.TimeField(max_length=45)),
                ('hora_termino', models.TimeField(max_length=45)),
                ('cantidad_personas', models.CharField(max_length=45)),
                ('estado', models.CharField(choices=[('Reservada', 'Reservada'), ('Confirmada', 'Confirmada')], default='Reservada', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Sala_reuniones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('ubicacion', models.CharField(blank=True, max_length=45, null=True)),
                ('capacidad', models.IntegerField()),
                ('horario_disponible', models.DateTimeField(blank=True, max_length=45, null=True)),
                ('estados', models.CharField(choices=[('No Disponible', 1), ('Disponible', 2), ('Reservada', 3), ('Confirmada', 4)], default='Disponible', max_length=10)),
                ('insumos', models.ManyToManyField(related_name='sala_reuniones_requests_created', to='app_site.Insumos')),
            ],
        ),
    ]
