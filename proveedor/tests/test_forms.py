
from django.test import TestCase
from ..forms import *
from ..models import *

class TestForms(TestCase):
    def test_proveedor_form_valid_data(self):
        print('>> TEST DE FORM DE PROVEEDOR VALIDO')
        print('')
        form = ProveedorForm(data={
            'cuit': '20-34567556-1',
            'nombre': 'Maria Angeles, Escalada',
            'email': 'maria-ang@gmail.com.ar',
            'telefono': '+54 9 11 45673456',
            'provincia': 'Parana',
            'localidad': 'Moreno',
            'calle': 'Calle falsa 1',
            'numero': 234,
            'responsableInscripto': 'Responsable no inscripto',
        })

        self.assertTrue(form.is_valid())

    def test_proveedor_form_invalid_data(self):
        direccion = Direccion.objects.create(
            provincia='Buenos Aires',
            localidad='Moreno',
            calle='Calle falsa 1',
            numero='234',
        )
        self.proveedor = Proveedor.objects.create(
            cuit='20-36786698-7',
            nombre='Juan Rodriguez',
            email='j.r@hotmail.com',
            telefono='(0237) 46673456',
            direccion=direccion,
            responsableInscripto='Responsable no inscripto'
        )
        print('>> TEST DE FORM DE PROVEEDOR INVALIDO POR CUIT REPETIDO')
        print('')
        form = ProveedorForm(data={
            'cuit': '20-36786698-7',
            'nombre': 'Maria Angeles, Escalada',
            'email': 'maria-ang@gmail.com.ar',
            'telefono': '+54 9 11 45673456',
            'provincia': 'Parana',
            'localidad': 'Moreno',
            'calle': 'Calle falsa 1',
            'numero': 234,
            'responsableInscripto': 'Responsable no inscripto',
        })

        self.assertFalse(form.is_valid())