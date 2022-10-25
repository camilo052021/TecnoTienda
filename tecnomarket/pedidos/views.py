from django.shortcuts import render, HttpResponse
# Importamos el modelo de datos de productos:
from .models import Producto, Categoria
from django.views.generic import ListView

# Create your views here.
'''def catalogo(request):
    # Query a la base de datos:
    productos = Producto.objects.all()
    template = 'pedidos/catalogo.html'
    context = {'productos': productos}

    return render(request, template, context)'''

    

class Catalogo(ListView):
    model = Producto
    template_name = 'pedidos/catalogo.html'
    

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'pedidos/barcatalogo.html'

