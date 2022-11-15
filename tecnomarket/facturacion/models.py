from django.db import models
# Importamos el modelo de datos de usuario:
from django.contrib.auth.models import User

from pedidos.models import Producto
# importamos los choices
from .choices import formapago, bancos

# importamos el perfil del usuario
from registration.models import PerfilUsuario

# Create your models here.
class FormaPago(models.Model):
    nombre_forma = models.CharField(verbose_name='Forma de Pago', choices= formapago, default = 'otro', max_length = 50)

    class Meta:
        verbose_name_plural = "Formas de pago"

    def __str__(self) -> str:
        return f'{self.nombre_forma}'

class DetallePago(models.Model):
    forma_pago = models.ForeignKey(FormaPago, on_delete=models.CASCADE)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    banco = models.CharField(verbose_name = 'Banco', choices = bancos, default = 'Otro', max_length = 50)
    cc_titular = models.CharField(verbose_name =  'Número de documento', max_length= 20)
    titular = models.CharField(verbose_name = 'Nombre titular de la cuenta', max_length = 150)
    total_pago = models.DecimalField(verbose_name = 'Total a Pagar', max_digits = 20, decimal_places = 2)
    iva_pago = models.DecimalField(verbose_name = 'IVA a pagar', max_digits = 20, decimal_places = 2)
  # Atributos de Auditoria:
    created = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)  
    updated = models.DateField(auto_now=True, verbose_name="Actualizado el")

    
    # def calculo_iva(self):
    #     iva_pago = float((self.total_pago / 1.19))
    #     return iva_pago
    # def save(self):
    #     self.iva_pago = float(self.calculo_iva)
    #     super (DetallePago, self).save()
    def valorIva(self):
        self.iva_pago = self.total_pago / 1.19
        return self.iva_pago
        
    class Meta:
        verbose_name_plural ='Detalle Pago'

    def __str__(self):
        return f'{self.cliente} {self.total_pago}' 


class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.CharField(max_length=15)
    cantidad = models.IntegerField(default=1)
    total =  models.DecimalField(verbose_name = 'Total', max_digits = 20, decimal_places = 2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cantidad} unidades de {self.producto.nombre_producto}"

    class Meta:
        db_table = 'pedidos'
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['id']


# class Factura(models.Model):
#     detalle = models.ForeignKey(DetallePago, on_delete=models.CASCADE)
#     cliente = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
#     producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
#     cantidad = models.IntegerField(verbose_name = 'Cantidad')
#     precio_unitario = models.DecimalField(verbose_name = 'Precio Unitario', max_digits = 20, decimal_places = 2)
#     valor = models.DecimalField(verbose_name = 'Valor Items', max_digits = 20, decimal_places = 2)
#     subtotal = models.DecimalField(verbose_name = 'Subtotal', max_digits = 20, decimal_places = 2)
#     total = models.DecimalField(verbose_name = 'Total', max_digits = 20, decimal_places = 2)
#     iva_pago = models.DecimalField(verbose_name = 'IVA a pagar', max_digits = 20, decimal_places = 2)
#     fecha_factura = models.DateField(auto_now_add=True, verbose_name="Fecha Facturación", null=True)  
#   # Atributos de Auditoria:
#     created = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)  
#     updated = models.DateField(auto_now=True, verbose_name="Actualizado el")