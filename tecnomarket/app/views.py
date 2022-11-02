from django.shortcuts import render

# importamos paquetes de vistas de clases:
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'app/home.html'

# atributos propios:
    context = {'titulo': 'Tienda Virtual'}

# Utilizando los métodos de la clase, sobreescribios get:
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)