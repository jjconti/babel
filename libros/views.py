# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import mixins, viewsets

from libros.models import Libro
from libros.serializers import LibrosSerializer


class LibrosViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    API endpoint para listar libros.
    """
    queryset = Libro.objects.all().order_by('titulo')
    serializer_class = LibrosSerializer
