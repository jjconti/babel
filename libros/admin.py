# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from libros.models import Autor, Libro


class AutorAdmin(admin.ModelAdmin):
    search_fields = ('nombre', 'apellido')


class LibroAdmin(admin.ModelAdmin):
    search_fields = ('titulo',)


admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, LibroAdmin)
