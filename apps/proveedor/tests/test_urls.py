from django.test import SimpleTestCase
from django.urls import reverse, resolve
from apps.proveedor.views import ProveedorList, ProveedorNew, ProveedorEdit, ProveedorDelete, ProveedorView

class TestUrls(SimpleTestCase):
    print('')
    print('--- TESTS EJECUTADOS ---')
    print('')

    def test_proveedor_list_url_resolves(self):
        url = reverse('proveedor:proveedor_list')
        self.assertEquals(resolve(url).func.view_class, ProveedorList)
        print('>> TEST DE URL DE LISTA DE PROVEEDORES')
        print('')

    def test_proveedor_new_resolves(self):
        url = reverse('proveedor:proveedor_new')
        self.assertEquals(resolve(url).func.view_class, ProveedorNew)
        print('>> TEST DE URL DE NUEVO PROVEEDOR')
        print('')


    def test_proveedor_edit_resolves(self):
        url = reverse('proveedor:proveedor_edit', args=['1'])
        self.assertEquals(resolve(url).func.view_class, ProveedorEdit)
        print('>> TEST DE URL DE EDITAR PROVEEDOR')
        print('')

    def test_proveedor_delete_resolves(self):
        url = reverse('proveedor:proveedor_delete', args=['1'])
        self.assertEquals(resolve(url).func.view_class, ProveedorDelete)
        print('>> TEST DE URL DE ELIMINAR PROVEEDOR')
        print('')

    def test_proveedor_view_resolves(self):
        url = reverse('proveedor:proveedor_view', args=['1'])
        self.assertEquals(resolve(url).func.view_class, ProveedorView)
        print('>> TEST DE URL DE DETALLE DE PROVEEDOR')
        print('')