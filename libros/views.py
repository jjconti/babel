# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import mixins, viewsets, filters, pagination

from libros.models import Libro
from libros.serializers import LibrosSerializer


class ConfigurablePagination(pagination.PageNumberPagination):
    page_size = 10


class LibrosViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    API endpoint para listar libros.
    """
    queryset = Libro.objects.all().order_by('titulo')
    serializer_class = LibrosSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('titulo', 'autor__nombre', 'autor__apellido')
    pagination_class = ConfigurablePagination
