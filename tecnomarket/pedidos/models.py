from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import CASCADE
import os
# Create your models here.

def subirImagenProducto(instance, filename):
    old_instance = Producto.objects.get(pk=instance.pk)
    #validamos si existe la imagen anterior
    if old_instance.imagen_producto:
        # asignamos una variable para el manejo del arrchivo:
        imagen = old_instance.imagen_producto
        # Validamos si efectivamente es un archivo:
        if imagen.file:
            # Si es un archivo,tomaremos su ubicación:
            if os.path.isfile(imagen.path):
                #cerramos el archivo si se encuentra en uso
                imagen.file.close()
                # Eliminamos el archivo usando los métodos del sistema operativo:
                os.remove(imagen.path)

    old_instance.imagen_producto.delete()
    return 'static/img/produtos/' + filename

class Categoria(models.Model):
    # atributos propios
    nombre_categoria = models.CharField(verbose_name = 'Nombre de Categoría', max_length = 50)
    # Atributos de Auditoria:
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha Actualización')

    class Meta:
        verbose_name_plural = 'Categoria'

    def __str__(self):
        return f'{self.nombre_categoria}'
    

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete = CASCADE)
    nombre_producto = models.CharField(verbose_name = 'Nombre', max_length=50)
    descripcion_producto = models.TextField(verbose_name = 'Descripción', null = True, blank = True)
    imagen_producto = models.ImageField(verbose_name = 'Imagen Producto', upload_to = subirImagenProducto, null = True, blank = True)
    costo_producto = models.DecimalField(verbose_name = 'Costo Producto', max_digits = 20, decimal_places = 2)
    precio = models.DecimalField(verbose_name = 'Precio', max_digits = 20, decimal_places = 2)
    cant_stock = models.IntegerField(verbose_name = 'Cantidada Disponible', validators=[MinValueValidator(0), MaxValueValidator(9999)])
    disponibilidad = models.BooleanField(default=True)
    # Atributos de Auditoria:
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha Actualización')

    class Meta:
        verbose_name_plural = 'Productos'
    def __str__(self):
        return f'{self.nombre_producto}'

       