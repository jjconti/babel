# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from libros.libros_factories import LibroFactory


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
