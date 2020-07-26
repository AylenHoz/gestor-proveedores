# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import *

app_name = 'proveedor'
urlpatterns = [
    url(r'^list/', login_required(ProveedorList.as_view()), name='proveedor_list'),
    url(r'^new$', login_required(ProveedorNew.as_view()), name='proveedor_new'),
    url(r'^edit/(?P<pk>\d+)$', login_required(ProveedorEdit.as_view()), name='proveedor_edit'),
    url(r'^delete/(?P<pk>\d+)$', login_required(ProveedorDelete.as_view()), name='proveedor_delete'),
    url(r'^detail/(?P<pk>\d+)$', login_required(ProveedorView.as_view()), name='proveedor_view'),
]