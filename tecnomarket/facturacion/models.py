from django.db import models
# Importamos el modelo de datos de usuario:
from django.contrib.auth.models import User
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

    @property
    def calculo_iva(self):
        iva_pago = (self.total_pago * 0.19)
        return iva_pago
    def save(self):
        self.iva_pago = self.calculo_iva
        super (DetallePago, self).save()

    class Meta:
        verbose_name_plural ='Detalle Pago'

    def __str__(self):
        return f'{self.cliente} {self.total_pago}' 



class Factura(models.Model):
    detalle = models.ForeignKey(DetallePago, on_delete=models.CASCADE)
    cliente = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    item = models.CharField(verbose_name = 'Producto', max_length = 150)
    cantidad = models.IntegerField(verbose_name = 'Cantidad')
    precio_unitario = models.DecimalField(verbose_name = 'Precio Unitario', max_digits = 20, decimal_places = 2)
    valor = models.DecimalField(verbose_name = 'Valor Items', max_digits = 20, decimal_places = 2)
    subtotal = models.DecimalField(verbose_name = 'Subtotal', max_digits = 20, decimal_places = 2)
    total = models.DecimalField(verbose_name = 'Total', max_digits = 20, decimal_places = 2)
    iva_pago = models.DecimalField(verbose_name = 'IVA a pagar', max_digits = 20, decimal_places = 2)
    fecha_factura = models.DateField(auto_now_add=True, verbose_name="Fecha Facturación", null=True)  
  # Atributos de Auditoria:
    created = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)  
    updated = models.DateField(auto_now=True, verbose_name="Actualizado el")