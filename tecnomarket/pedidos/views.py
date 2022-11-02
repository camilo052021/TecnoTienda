
from django.shortcuts import render, HttpResponse, redirect


from pedidos.carro import Carro
# Importamos el modelo de datos de productos:
from pedidos.models import Producto, Categoria
from django.views.generic import ListView, TemplateView


class Catalogo(ListView):
    model = Producto
    template_name = 'pedidos/catalogo.html'

def agregarProducto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect ('catalogo')

def eliminarProducto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect('carro')

def restarProducto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.restarProducto(producto=producto)
    return redirect('carro')

def limpiarCarro(request):
    carro = Carro(request)
    carro.limpiarCarro()
    return redirect('catalogo')

def carro(request):
    return render(request, 'pedidos/carro.html')




