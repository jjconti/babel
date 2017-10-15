# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers

from libros.views import LibrosViewSet

router = routers.DefaultRouter()
router.register(r'libros', LibrosViewSet, base_name='libros')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
]
