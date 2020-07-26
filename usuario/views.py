# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import CreateView
from .forms import *

class RegistroUsuario(CreateView):
    model = User
    template_name = 'usuario/registrar.html'
    form_class = RegistroForm
    success_url = reverse_lazy('home')