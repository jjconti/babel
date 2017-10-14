# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from libros.models import Libro


class LibrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ('titulo', 'nombre_autor', 'fecha_publicacion')
