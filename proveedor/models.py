# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

categorias = [('', 'Seleccione una categoría'),
              ('Responsable no inscripto', 'Responsable no inscripto'),
              ('Responsable inscripto - Categoría A', 'Responsable inscripto - Categoría A'),
              ('Responsable inscripto - Categoría B', 'Responsable inscripto - Categoría B'),
              ('Responsable inscripto - Categoría C', 'Responsable inscripto - Categoría C'),
              ('Responsable inscripto - Categoría D', 'Responsable inscripto - Categoría D'),
              ('Monotributista - Categoría A', 'Monotributista - Categoría A'),
              ('Monotributista - Categoría B', 'Monotributista - Categoría B'),
              ('Monotributista - Categoría C', 'Monotributista - Categoría C'),
              ('Monotributista - Categoría D', 'Monotributista - Categoría D'),
              ('Monotributista - Categoría E', 'Monotributista - Categoría E'),
              ('Monotributista - Categoría F', 'Monotributista - Categoría F'),
]

provincias = [('', 'Seleccione una provincia'),
              ('Buenos Aires', 'Buenos Aires'),
              ('Catamarca', 'Catamarca'),
              ('Chaco', 'Chaco'),
              ('Chubut', 'Chubut'),
              ('Cordoba', 'Cordoba'),
              ('Corrientes', 'Corrientes'),
              ('Entre Rios', 'Entre Rios'),
              ('Formosa', 'Formosa'),
              ('Jujuy', 'Jujuy'),
              ('La Pampa', 'La Pampa'),
              ('La Rioja', 'La Rioja'),
              ('Mendoza', 'Mendoza'),
              ('Misiones', 'Misiones'),
              ('Neuquen', 'Neuquen'),
              ('Rio Negro', 'Rio Negro'),
              ('Salta', 'Salta'),
              ('San Juan', 'San Juan'),
              ('San Luis', 'San Luis'),
              ('Santa Cruz', 'Santa Cruz'),
              ('Santa Fe', 'Santa Fe'),
              ('Tierra del Fuego', 'Tierra del Fuego'),
              ('Tucuman', 'Tucuman'),
]

class Direccion(models.Model):
    provincia = models.CharField(max_length=100, default="", choices=provincias)
    localidad = models.CharField(max_length=50)
    calle = models.CharField(max_length=50)
    numero = models.CharField(max_length=50)

class Proveedor(models.Model):
    cuit = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    direccion = models.OneToOneField(Direccion, null=False, blank=False, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=100)
    responsableInscripto = models.CharField(max_length=100, default="", choices=categorias)