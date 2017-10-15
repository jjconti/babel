# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime, timedelta
import string

import factory
from factory import fuzzy

from libros.models import Autor, Libro

TWENTY_YEARS_AGO = datetime.now() - timedelta(days=20 * 365)
FIFTY_YEARS_AGO = datetime.now() - timedelta(days=50*365)


class AutorFactory(factory.django.DjangoModelFactory):
    """
    Factory de objectos Autor para usar en los tests.
    """
    nombre = fuzzy.FuzzyText()
    apellido = fuzzy.FuzzyText()
    fecha_nacimiento = fuzzy.FuzzyDate(FIFTY_YEARS_AGO, TWENTY_YEARS_AGO)

    class Meta:
        model = Autor
        django_get_or_create = ('nombre', 'apellido')


class LibroFactory(factory.django.DjangoModelFactory):
    """
    Factory de objectos Libro para usar en los tests.
    """
    titulo = fuzzy.FuzzyText(chars=string.ascii_uppercase)
    autor = factory.SubFactory(AutorFactory)
    fecha_publicacion = fuzzy.FuzzyDate(TWENTY_YEARS_AGO, datetime.now())

    class Meta:
        model = Libro
        django_get_or_create = ('titulo',)
