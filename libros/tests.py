# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.core.urlresolvers import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from libros.libros_factories import LibroFactory, AutorFactory


class LibrosTestCase(TestCase):
    client_class = APIClient

    def setUp(self):
        for x in range(10):
            LibroFactory()

    def test_list(self):
        url = reverse('libros-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(len(data), 10)

    def test_list_sorted_by_title(self):
        url = reverse('libros-list')
        response = self.client.get(url)
        data = response.json()
        titulos = [l['titulo'] for l in data]
        self.assertEqual(titulos, sorted(titulos))


class SearchLibrosTestCase(TestCase):
    client_class = APIClient

    def setUp(self):
        oyola = AutorFactory(nombre="Leonardo", apellido="Oyola")
        LibroFactory(titulo="Siete y el tigre harapiento", autor=oyola)
        LibroFactory(titulo="Nunca corrí siempre cobré", autor=oyola)
        LibroFactory(titulo="Chamamé", autor=oyola)

        martin = AutorFactory(nombre="Martín", apellido="Castagnet")
        LibroFactory(titulo="Los cuerpos del verano", autor=martin)

    def test_list_search_autor(self):
        url = reverse('libros-list')
        url += '?search={}'
        response = self.client.get(url.format('oyo'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(data), 3)
        self.assertEqual(data[0]['titulo'], "Chamamé")
        self.assertEqual(data[0]['nombre_autor'], "Leonardo Oyola")
        self.assertEqual(data[1]['titulo'], "Nunca corrí siempre cobré")
        self.assertEqual(data[1]['nombre_autor'], "Leonardo Oyola")
        self.assertEqual(data[2]['titulo'], "Siete y el tigre harapiento")
        self.assertEqual(data[2]['nombre_autor'], "Leonardo Oyola")

    def test_list_search_title_autor(self):
        url = reverse('libros-list')
        url += '?search={}'
        response = self.client.get(url.format('ma'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['titulo'], "Chamamé")
        self.assertEqual(data[0]['nombre_autor'], "Leonardo Oyola")
        self.assertEqual(data[1]['titulo'], "Los cuerpos del verano")
        self.assertEqual(data[1]['nombre_autor'], "Martín Castagnet")
