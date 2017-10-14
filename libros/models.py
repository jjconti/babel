# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Autor(models.Model):

    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    fecha_nacimiento = models.DateField()


class Libro(models.Model):

    titulo = models.CharField(max_length=250)
    fecha_publicacion = models.DateField()
    autor = models.ForeignKey(Autor)
