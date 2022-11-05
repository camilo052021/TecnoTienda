from django.shortcuts import render, redirect, HttpResponse
from carro.carro import Carro
# Importamos el modelo de datos de productos:
from pedidos.models import Producto


def agregar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect("catalogo")

def eliminar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("carro")

def restar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("carro")

def limpiar_carro(request):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect("catalogo")

def carro(request):
    return render(request, 'carro/carro.html')


