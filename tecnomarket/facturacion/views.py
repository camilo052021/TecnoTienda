import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import HttpResponse, redirect, render
from django.views.generic import ListView, View
from django.views.generic.edit import CreateView
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

from carro.carro import Carro
from carro.context_processor import carritoCompras
from registration.models import PerfilUsuario

from .forms import DetallePagoForm
from .models import DetallePago, Pedido
from .utils import render_to_pdf  # created in step 4

# Create your views here.

def factura(request):
    fecha = datetime.datetime.now()
    carro = Carro(request)
    context = {
        'fecha':fecha,
        'carro':carro,
    }
    return render(request, 'facturacion/factura.html', context)



class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        datos = User.objects.get(username=request.user.username)
        perfil = PerfilUsuario.objects.get(id=request.user.id)
        fecha = datetime.datetime.today()
        carro = Carro(request)
        pagos = DetallePago.objects.filter(id=request.user.id)
        data = {
            'fecha':fecha,
            'carro':carro,
            'datos':datos,
            'perfil':perfil,
            'pagos':pagos,
        }
        pdf = render_to_pdf('facturacion/pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')



# class PasarelaPago(CreateView):
#     template_name = 'facturacion/pago.html'
#     form_class = DetallePagoForm
#     success_url = '/'


def pago(request):  
    if request.method == 'POST':
        carro=Carro(request)
        form = DetallePagoForm(request.POST)
        if form.is_valid():
            form.save()
            carro.limpiar_carro()
            return redirect('/')
    else:
        form = DetallePagoForm()
  
    context = {'form': form}
    return render(request, 'facturacion/pago.html', context)


@login_required(login_url="/registration/login")
def procesar_pedido(request):
    carro = Carro(request)
    pedido = carritoCompras(request)['consecutivo']
    lineas_pedido = list()
    
    
    for key, value in carro.carro.items():
        lineas_pedido.append(Pedido(
            producto_id=key,
            cantidad=value['cantidad'],
            total=value['subtotal'],
            user=request.user,
            pedido=pedido
        ))
    
    Pedido.objects.bulk_create(lineas_pedido)

    enviar_mail(
        pedido=pedido,
        nombreusuario=request.user.username,
        emailusuario=request.user.email
    )

    messages.success(request, "El pedido se procesó correctamente")
    carro.limpiar_carro()
    return redirect('/')


def enviar_mail(**kwargs):
    asunto="Gracias por hacer el pedido"
    mensaje = render_to_string("facturacion/factura.html",{
        "pedido": kwargs.get("pedido"),
        "nombreusuario": kwargs.get("nombreusuario")
    })

    mensaje_texto = strip_tags(mensaje)
    from_email="camand5@une.net.co"
    to=kwargs.get("emailusuario")

    send_mail(
        asunto,
        mensaje_texto,
        from_email,
        [to],
        html_message=mensaje
    )
