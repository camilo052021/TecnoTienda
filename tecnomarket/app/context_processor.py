# Importamos el modelo de datos de productos:
from multiprocessing import context
from pedidos.models import Categoria, Marca

def categoria(request):
    # Query a la base de datos:
    categorias = Categoria.objects.all()
    marcas = Marca.objects.all()
    context = {
        'categorias':categorias,
        'marcas':marcas,
    }
    return context