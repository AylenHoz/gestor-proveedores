from django.test import TestCase, Client
from django.urls import reverse
from apps.proveedor.models import Proveedor, Direccion

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        direccion = Direccion.objects.create(
            provincia='Buenos Aires',
            localidad='Moreno',
            calle='Calle falsa 1',
            numero='234',
        )
        self.proveedor = Proveedor.objects.create(
            cuit='20-36789998-5',
            nombre='Juan Rodriguez',
            email='j.r@hotmail.com',
            telefono='(0237) 46673456',
            direccion=direccion,
            responsableInscripto='Responsable no inscripto'
        )
        self.list_url = reverse('proveedor:proveedor_list')
        self.edit_url = reverse('proveedor:proveedor_edit', args=[self.proveedor.pk])
        self.view_url = reverse('proveedor:proveedor_view', args=[self.proveedor.pk])
        self.delete_url = reverse('proveedor:proveedor_delete', args=[self.proveedor.pk])
        self.new_url = reverse('proveedor:proveedor_new')

    def test_proveedor_list_GET(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'proveedor/list.html')
        print('>> TEST DE VIEW DE LISTA DE PROVEEDORES (GET)')
        print('')

    def test_proveedor_new_GET(self):
        response = self.client.get(self.new_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'proveedor/form.html')
        print('>> TEST DE VIEW DE NUEVO PROVEEDOR (GET)')
        print('')

    def test_proveedor_new_POST(self):
        test_direccion = Direccion.objects.create(
            provincia='Mendoza',
            localidad='Moreno',
            calle='Calle falsa 1',
            numero=234,
        )
        print('>> TEST DE VIEW DE NUEVO PROVEEDOR (POST)')
        print('')
        response = self.client.post(self.new_url, {
            'cuit': '27-34567556-1',
            'nombre': 'Maria Angeles, Escalada',
            'email': 'maria-ang@gmail.com.ar',
            'telefono': '+54 9 11 45673456',
            'provincia': 'Mendoza',
            'localidad': 'Moreno',
            'calle': 'Calle falsa 1',
            'numero': 234,
            'responsableInscripto': 'Responsable no inscripto',
        })
        self.assertEquals(response.status_code, 302)

    def test_proveedor_edit_GET(self):
        response = self.client.get(self.edit_url)
        print('>> TEST DE VIEW DE EDITAR PROVEEDOR (GET)')

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'proveedor/form.html')
        print('El id del proveedor es ' + str(self.proveedor.pk))
        print('')

    def test_proveedor_edit_POST(self):
        print('>> TEST DE VIEW DE EDITAR PROVEEDOR (POST)')
        response = self.client.post(self.edit_url, {
            'cuit': self.proveedor.cuit,
            'nombre': 'Maria, Escalada',
            'email': 'mari@outlook.com',
            'telefono': '34563456',
            'provincia': 'Buenos Aires',
            'localidad': self.proveedor.direccion.localidad,
            'calle': 'Calle falsa 1',
            'numero': 234,
            'responsableInscripto': self.proveedor.responsableInscripto,
        })
        self.assertEquals(response.status_code, 302)

    def test_proveedor_delete_DELETE(self):
        response = self.client.post(self.delete_url, {
            'id': self.proveedor.pk
        })
        self.assertEquals(response.status_code, 302)

    def test_proveedor_view_GET(self):
        response = self.client.get(self.view_url)
        print('>> TEST DE VIEW DE DETALLE DE PROVEEDOR (GET)')
        print('El id del proveedor es ' + str(self.proveedor.pk))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'proveedor/form.html')
        print('')