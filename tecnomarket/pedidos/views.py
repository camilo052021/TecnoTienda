
from django.shortcuts import render, redirect, HttpResponse
# Importamos el modelo de datos de productos:
from pedidos.models import Producto, Categoria,Marca
from django.views.generic import ListView, TemplateView


class Catalogo(ListView):
    model = Producto
    template_name = 'pedidos/catalogo.html'
    paginate_by = 8

def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    productos = Producto.objects.filter(categoria=categoria)
    context  ={'productos': productos, 'categoria': categoria}
    return render(request, 'pedidos/categorias.html', context) 

# def marca(request, marca_id):
#     marca = Marca.objects.get(id=marca_id)
#     productos = Producto.objects.filter(marca=marca)
#     context  ={'productos': productos, 'marca': marca}
#     return render(request, 'pedidos/marcas.html', context) 

