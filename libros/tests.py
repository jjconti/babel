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
        self.assertEqual(len(data['results']), 10)

    def test_list_sorted_by_title(self):
        url = reverse('libros-list')
        response = self.client.get(url)
        data = response.json()
        titulos = [l['titulo'] for l in data['results']]
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
        self.assertEqual(len(data['results']), 3)
        self.assertEqual(data['results'][0]['titulo'], "Chamamé")
        self.assertEqual(data['results'][0]['nombre_autor'], "Leonardo Oyola")
        self.assertEqual(data['results'][1]['titulo'], "Nunca corrí siempre cobré")
        self.assertEqual(data['results'][1]['nombre_autor'], "Leonardo Oyola")
        self.assertEqual(data['results'][2]['titulo'], "Siete y el tigre harapiento")
        self.assertEqual(data['results'][2]['nombre_autor'], "Leonardo Oyola")

    def test_list_search_title_autor(self):
        url = reverse('libros-list')
        url += '?search={}'
        response = self.client.get(url.format('ma'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(data['results']), 2)
        self.assertEqual(data['results'][0]['titulo'], "Chamamé")
        self.assertEqual(data['results'][0]['nombre_autor'], "Leonardo Oyola")
        self.assertEqual(data['results'][1]['titulo'], "Los cuerpos del verano")
        self.assertEqual(data['results'][1]['nombre_autor'], "Martín Castagnet")


class PaginationLibrosTestCase(TestCase):
    client_class = APIClient

    def setUp(self):
        for x in range(100):
            LibroFactory()

    def test_pagination(self):
        url = reverse('libros-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data['count'], 100)
        self.assertEqual(len(data['results']), 10)
        self.assertIsNone(data['previous'])
        self.assertIsNotNone(data['next'])

        response = self.client.get(data['next'])
        data = response.json()
        self.assertEqual(data['count'], 100)
        self.assertEqual(len(data['results']), 10)
        self.assertIsNotNone(data['previous'])
        self.assertIsNotNone(data['next'])

    def test_pagination_page_size(self):
        url = reverse('libros-list')
        url += '?page_size={}'
        response = self.client.get(url.format(50))
        data = response.json()
        self.assertEqual(data['count'], 100)
        self.assertEqual(len(data['results']), 50)
        self.assertIsNone(data['previous'])
        self.assertIsNotNone(data['next'])

        response = self.client.get(data['next'])
        data = response.json()
        self.assertEqual(data['count'], 100)
        self.assertEqual(len(data['results']), 50)
        self.assertIsNotNone(data['previous'])
        self.assertIsNone(data['next'])
