from django.db import models

# Create your models here.

class Contacto(models.Model):
    nombre = models.CharField(verbose_name = 'Nombre', max_length = 50)
    email = models.EmailField(verbose_name = 'Correo')
    mensaje = models.TextField(verbose_name = 'Mensaje')
    atendido = models.BooleanField(verbose_name = 'Atendido', default = False)
    # Atributos de Auditoria:
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha Actualización')

    class Meta:
        verbose_name_plural = 'Contacto'

    def __str__(self):
        return f'{self.nombre}'