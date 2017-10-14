# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from libros.models import Autor, Libro


class AutorAdmin(admin.ModelAdmin):
    pass


class LibroAdmin(admin.ModelAdmin):
    pass


admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, LibroAdmin)
