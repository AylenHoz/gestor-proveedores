# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url
from .views import *

app_name = 'usuario'
urlpatterns = [
    url(r'^registrar', RegistroUsuario.as_view(), name='registrar'),
]