# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models.functions import Lower
from django.shortcuts import render

from rest_framework import mixins, viewsets, filters, pagination

from libros.models import Libro
from libros.serializers import LibrosSerializer


class ConfigurablePagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'


class LibrosViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    API endpoint para listar libros.
    """
    queryset = Libro.objects.all().order_by(Lower('titulo'))
    serializer_class = LibrosSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('titulo', 'autor__nombre', 'autor__apellido')
    pagination_class = ConfigurablePagination


def libros_list(request):
    return render(request, 'libros.html', {})
