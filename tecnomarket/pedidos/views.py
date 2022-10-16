from multiprocessing import context
from re import template
from django.shortcuts import render, HttpResponse
# Importamos el modelo de datos de productos:
from .models import Producto, Categoria

# Create your views here.
def catalogo(request):
    # Query a la base de datos:
    productos = Producto.objects.all()
    template = 'pedidos/catalogo.html'
    context = {'productos': productos}

    return render(request, template, context)