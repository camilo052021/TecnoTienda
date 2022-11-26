import json
from django.shortcuts import render, redirect, HttpResponse
# Importamos el modelo de datos de productos:
from pedidos.models import Producto, Categoria,Marca
from django.views.generic import ListView, TemplateView


from django.forms.models import model_to_dict

from django.http import JsonResponse
from django.views import View



class CatalogoApiResponse(View):
    # query a la base de datos
    productos = Producto.objects.all()
    # cast de prudcutos para voverlos un arreglo
    productos = list(productos.values())

    # definimos los metodos
    def get(self, request):
        return JsonResponse(self.productos, safe=False)


class ProductoApiResponse(View):
    #definimos le método
    def get(self, request, pk):
        #query a la base de datos
        producto = Producto.objects.get(pk=pk)
        producto = model_to_dict(producto)
        producto['imagen_producto'] = json.dumps(str(producto['imagen_producto'] ))
        return JsonResponse(producto, safe=False)


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

