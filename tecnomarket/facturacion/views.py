from django.shortcuts import render
from registration.models import PerfilUsuario
import datetime

# Create your views here.

def factura(request):
    fecha = datetime.datetime.now()
    context = {
        'fecha':fecha
    }
    return render(request, 'pdf/pdf.html', context)