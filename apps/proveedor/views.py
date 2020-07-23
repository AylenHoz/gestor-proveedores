# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from models import Proveedor, Direccion
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from forms import ProveedorForm, DireccionForm


def index(request):
    return render(request, 'home/home.html')

class ProveedorList(ListView):
    model = Proveedor
    template_name = 'proveedor/list.html'
    ordering = ['nombre']
    paginate_by = 5

class ProveedorNew(CreateView):
    model = Proveedor
    template_name = 'proveedor/form.html'
    form_class = ProveedorForm
    second_form_class = DireccionForm
    success_url = reverse_lazy('proveedor:proveedor_list')

    def get_context_data(self, **kwargs):
        context = super(ProveedorNew, self).get_context_data(**kwargs)
        context['action'] = 'Nuevo'
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            proveedor = form.save(commit=False)
            proveedor.direccion = form2.save()
            proveedor.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))

class ProveedorEdit(UpdateView):
    model = Proveedor
    second_model = Direccion
    template_name = 'proveedor/form.html'
    form_class = ProveedorForm
    second_form_class = DireccionForm
    success_url = reverse_lazy('proveedor:proveedor_list')

    def get_context_data(self, **kwargs):
        context = super(ProveedorEdit, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        proveedor = self.model.objects.get(id=pk)
        direccion = self.second_model.objects.get(id=proveedor.direccion_id)
        context['action'] = 'Editar'
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=direccion)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_proveedor = kwargs['pk']
        proveedor = self.model.objects.get(id=id_proveedor)
        direccion = self.second_model.objects.get(id=proveedor.direccion_id)
        form = self.form_class(request.POST, instance=proveedor)
        form2 = self.second_form_class(request.POST, instance=direccion)
        context = {"form": form,
                   "form2": form2,
                   "action": "Editar"}
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return render(request, "proveedor/form.html", context)

class ProveedorDelete(DeleteView):
    model = Proveedor
    template_name = 'proveedor/delete.html'
    success_url = reverse_lazy('proveedor:proveedor_list')

class ProveedorView(DetailView):
    model = Proveedor
    second_model = Direccion
    template_name = 'proveedor/form.html'
    form_class = ProveedorForm
    second_form_class = DireccionForm
    success_url = reverse_lazy('proveedor:proveedor_list')

    def get_context_data(self, **kwargs):
        context = super(ProveedorView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        proveedor = self.model.objects.get(id=pk)
        direccion = self.second_model.objects.get(id=proveedor.direccion_id)
        context['action'] = 'Detalle de '
        if 'form' not in context:
            context['form'] = self.form_class(instance=proveedor)
            context['form'].fields['cuit'].widget.attrs['readonly'] = True
            context['form'].fields['nombre'].widget.attrs['readonly'] = True
            context['form'].fields['email'].widget.attrs['readonly'] = True
            context['form'].fields['telefono'].widget.attrs['readonly'] = True
            context['form'].fields['responsableInscripto'].widget.attrs['disabled'] = True
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=direccion)
            context['form2'].fields['provincia'].widget.attrs['disabled'] = True
            context['form2'].fields['localidad'].widget.attrs['readonly'] = True
            context['form2'].fields['calle'].widget.attrs['readonly'] = True
            context['form2'].fields['numero'].widget.attrs['readonly'] = True
        context['id'] = pk
        return context

