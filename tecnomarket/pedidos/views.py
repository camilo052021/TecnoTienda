
# Importamos el modelo de datos de productos:
from .models import Producto, Categoria
from django.views.generic import ListView


class Catalogo(ListView):
    model = Producto
    template_name = 'pedidos/catalogo.html'






