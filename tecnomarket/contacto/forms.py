from django import forms
# importamos nuestro modelo
from .models import Contacto


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre','email','mensaje',]
        widgets = {
            'nombre_categoria' : forms.TextInput(attrs = {'class':'form-control mt-2'}),
            'email' : forms.TextInput(attrs = {'class':'form-control mt-2'}),
            'mensaje' : forms.Textarea(attrs = {'class':'form-control mt-2'}),
        }