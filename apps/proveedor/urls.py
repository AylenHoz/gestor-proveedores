# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url
from views import ProveedorList, ProveedorNew, ProveedorEdit, ProveedorDelete, ProveedorView

urlpatterns = [
    url(r'^list/', ProveedorList.as_view(), name='proveedor_list'),
    url(r'^new$', ProveedorNew.as_view(), name='proveedor_new'),
    url(r'^edit/(?P<pk>\d+)$', ProveedorEdit.as_view(), name='proveedor_edit'),
    url(r'^delete/(?P<pk>\d+)$', ProveedorDelete.as_view(), name='proveedor_delete'),
    url(r'^detail/(?P<pk>\d+)$', ProveedorView.as_view(), name='proveedor_view'),
]