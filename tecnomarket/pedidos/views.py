
from django.shortcuts import render, redirect, HttpResponse
# Importamos el modelo de datos de productos:
from pedidos.models import Producto, Categoria
from django.views.generic import ListView, TemplateView


class Catalogo(ListView):
    model = Producto
    template_name = 'pedidos/catalogo.html'
