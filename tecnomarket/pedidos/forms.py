from django import forms
# importamos nuestro modelo
from .models import Categoria, Producto

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre_categoria',]
        widgets = {
            'nombre_categoria' : forms.TextInput(attrs = {'class':'form-control mt-2'}),
        }


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['categoria','nombre_producto','descripcion_producto','imagen_producto','costo_producto','precio','cant_stock','disponibilidad']
        widgets = {
            'categoria' : forms.TextInput(attrs = {'class':'form-control mt-2'}),
            'nombre_producto' : forms.TextInput(attrs = {'class':'form-control mt-2'}),
            'descripcion_producto' : forms.Textarea(attrs = {'class':'form-control mt-2', 'rows': '3'}),
            'imagen_producto' : forms.ClearableFileInput(attrs = {'class':'form-control mt-2'}),
            'costo_producto' : forms.TextInput(attrs = {'class':'form-control mt-2'}),
            'precio' : forms.TextInput(attrs = {'class':'form-control mt-2'}),
            'cant_stock' : forms.TextInput(attrs = {'class':'form-control mt-2'}),
            'disponibilidad' : forms.BooleanField(attrs = {'class':'form-control mt-2'}),
        }
    
