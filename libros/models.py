# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Autor(models.Model):

    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    fecha_nacimiento = models.DateField()

    class Meta:
        verbose_name_plural = "autores"

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellido)


@python_2_unicode_compatible
class Libro(models.Model):

    titulo = models.CharField(max_length=250)
    fecha_publicacion = models.DateField()
    autor = models.ForeignKey(Autor)

    @property
    def nombre_autor(self):
        return unicode(self.autor)

    def __str__(self):
        return self.titulo
