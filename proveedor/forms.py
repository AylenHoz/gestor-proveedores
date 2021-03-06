#-*⁻ encoding: utf-8 -*-
from django import forms
from django.core.exceptions import ValidationError
import re
from .models import *

number_regex = '[0-9]'
char_regex = '[a-zA-Z]'
char_con_acentos_y_enie_regex = '(' + char_regex + '|ñ|Ñ|á|é|í|ó|ú|Á|É|Í|Ó|Ú|ä|ë|ï|ö|ü|Ä|Ë|Ï|Ö|Ü)'
space = '\s'

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = [
            'nombre',
            'cuit',
            'email',
            'telefono',
            'responsableInscripto'
        ]
        labels = {
            'nombre': 'Nombre/ y apellido/s',
            'cuit': 'CUIT',
            'email': 'Correo electrónico',
            'telefono': 'Teléfono/Celular',
            'responsableInscripto': 'Responsable inscripto',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'cuit': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'responsableInscripto': forms.Select(attrs={'class':'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProveedorForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].required = False
        self.fields['cuit'].required = False
        self.fields['email'].required = False
        self.fields['telefono'].required = False
        self.fields['responsableInscripto'].required = False

    def clean_cuit(self, *args, **kwargs):
        cuit = self.cleaned_data['cuit']
        if cuit == '':
            raise ValidationError(['Ingrese el CUIT del proveedor.',
                                   'Ejemplo: 27-37897667-7'])
        else:
            if len(str(cuit)) > 10:
                cuit_sin_guiones = re.sub('-', '', str(cuit))
                cuit_con_guiones = cuit_sin_guiones[0:2] + '-' + cuit_sin_guiones[2:10] + '-' + cuit_sin_guiones[10:11]
                coincidencias_cuit_1 = Proveedor.objects.all().filter(cuit=cuit_sin_guiones).exclude(pk=self.instance.id)
                coincidencias_cuit_2 = Proveedor.objects.all().filter(cuit=cuit_con_guiones).exclude(pk=self.instance.id)
                if len(coincidencias_cuit_1) == 0 and len(coincidencias_cuit_2) == 0:
                    begin = r'^((20)|(23)|(24)|(25)|(26)|(27)|(30)){1}'
                    regex1 = begin + number_regex + '{8}' + number_regex + '{1}$'
                    regex2 = begin + '-{1}' + number_regex + '{8}-{1}' + number_regex + '{1}$'
                    match1 = re.match(regex1, cuit.encode('utf-8'), 0)
                    match2 = re.match(regex2, cuit.encode('utf-8'), 0)
                    if match1 is not None or match2 is not None:
                        return cuit
                    raise ValidationError(['Ingrese un CUIT válido.',
                                       'Ejemplo: 27-37897667-7'])
                else:
                    raise ValidationError(['Ya existe un proveedor registrado con este cuit.',
                                       'Por favor, ingrese un CUIT válido',
                                       'Ejemplo: 27-37897667-7'])
            else:
                raise ValidationError(['Ingrese un CUIT válido.',
                                       'Ejemplo: 27-37897667-7'])

    def clean_nombre(self, *args, **kwargs):
        nombre = self.cleaned_data['nombre']
        if nombre == '':
            raise ValidationError(['Ingrese el nombre y apellido del proveedor.',
                                  'Ejemplo: Juan Rodriguez.'])
        else:
            regex = r'^(' + char_con_acentos_y_enie_regex + '{2,}' + '(' + space + '+' + char_con_acentos_y_enie_regex + '{2,}' + ')*(((,?'+ space + '+' +\
                    ')){1}('+ char_con_acentos_y_enie_regex + '{2,}' + '(' + space + '+' + char_con_acentos_y_enie_regex + '{2,}' + ')*)))$'
            match = re.match(regex, nombre.encode('utf-8'), 0)
            if match is not None:
                return nombre
            raise ValidationError(['Ingrese nombre/s y apellido/s válido/s.'
                                   'Ejemplo: Juan Rodriguez.'])

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data['email']
        if email == '':
            raise ValidationError(['Ingrese el email del proveedor.',
                                   'Se permiten letras, guiones y puntos.',
                                   'Ejemplo: example@correo.com.ar'])
        else:
            regex = r'^(' + char_regex + '{1}(-|_|\.|' + char_regex + ')*@' + char_regex +\
                    '+(\.' + char_regex + '+)+)$'
            match = re.match(regex, email.encode('utf-8'), 0)
            if match is not None:
                return email
            raise ValidationError(['Ingrese un correo válido.',
                                   'Se permiten letras, guiones y puntos.',
                                   'Ejemplo: example@correo.com.ar'
                                   ])

    def clean_telefono(self, *args, **kwargs):
        telefono = self.cleaned_data['telefono']
        if telefono == '':
            raise ValidationError(['Ingrese el teléfono del proveedor.',
                                   'Ejemplo: +54 9 11 6789-5670'])
        else:
            regex = r'^((((\(011\)' + space + '(' + number_regex +\
                '+' + space + ')*)|(\+(' + space + '?' + number_regex +\
                '+)+' + space + '))?((' + number_regex + '{4}-' + number_regex +\
                '{4})|(' + number_regex + '{8})))|(((\(' + number_regex + '+\))|((' + space + '?' + number_regex +\
                '+)+)' + space + ')?((' + number_regex + '{3}-' + number_regex +\
                '{4})|(' + number_regex + '{7}))))$'
            match = re.match(regex, telefono.encode('utf-8'), 0)
            if match is not None:
                return telefono
            raise ValidationError(['Ingrese un teléfono válido.',
                                   'Ejemplo: +54 9 11 6789-5670'])

    def clean_responsableInscripto(self, *args, **kwargs):
        responsableInscripto = self.cleaned_data['responsableInscripto']
        if responsableInscripto == '':
            raise ValidationError('Seleccione una categoría de responsable inscripto.')
        return responsableInscripto

class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = [
            'provincia',
            'localidad',
            'calle',
            'numero',
        ]
        labels = {
            'provincia': 'Provincia',
            'localidad': 'Localidad o partido',
            'calle': 'Calle',
            'numero': 'Nro.',
        }
        widgets = {
            'provincia': forms.Select(attrs={'class':'form-control'}),
            'localidad': forms.TextInput(attrs={'class':'form-control'}),
            'calle': forms.TextInput(attrs={'class':'form-control'}),
            'numero': forms.TextInput(attrs={'class':'form-control'}),
        }

    def __init__(self2, *args, **kwargs):
        super(DireccionForm, self2).__init__(*args, **kwargs)
        self2.fields['provincia'].required = False
        self2.fields['localidad'].required = False
        self2.fields['calle'].required = False
        self2.fields['numero'].required = False

    def clean_provincia(self, *args, **kwargs):
        provincia = self.cleaned_data['provincia']
        if provincia == '':
            raise ValidationError('Seleccione una provincia.')
        return provincia

    def clean_localidad(self, *args, **kwargs):
        localidad = self.cleaned_data['localidad']
        if localidad == '':
            raise ValidationError(['Ingrese una localidad o partido.',
                                   'Ejemplo: 3 de Febrero'])
        else:
            regex = r'^((' + space + '|' + char_con_acentos_y_enie_regex + '|' + number_regex + ')+)$'
            match = re.match(regex, localidad.encode('utf-8'), 0)
            if match is not None:
                return localidad
            raise ValidationError(['Ingrese una localidad o partido válido.',
                                   'Ejemplo: 3 de Febrero'])

    def clean_calle(self, *args, **kwargs):
        calle = self.cleaned_data['calle']
        if calle == '':
            raise ValidationError(['Ingrese una calle.',
                                   'Ejemplo: 25 de Mayo'])
        else:
            regex = r'^((' + space + '|' + char_con_acentos_y_enie_regex + '|' + number_regex + ')+)$'
            match = re.match(regex, calle.encode('utf-8'), 0)
            if match is not None:
                return calle
            raise ValidationError(['Ingrese una calle válida.',
                                   'Ejemplo: 25 de Mayo'])

    def clean_numero(self, *args, **kwargs):
        numero = self.cleaned_data['numero']
        if numero == '':
            raise ValidationError(['Ingrese el número correspondiente a la dirección.',
                                    'Ejemplo: 2500'])
        else:
            regex = r'^((' + number_regex + '|' + char_regex + '|' + space + ')+)$'
            match = re.match(regex, numero.encode('utf-8'), 0)
            if match is not None:
                return numero
            return ValidationError(['Ingrese el número válido correspondiente a la calle ingresada.',
                                    'Ejemplo: 2500'])