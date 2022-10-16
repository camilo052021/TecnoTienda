# Importar librerias
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models import fields
from django.forms import widgets

# importamos el modelo de datos personales Perfil
from .models import PerfilUsuario
class PerfilForm(forms.ModelForm):
    # Pasamos la metadata del formulario:    
    class Meta:
        model = PerfilUsuario
        fields = ['img_perfil','genero','tipo_documento','numero_documento','direccion','telefono','ciudad','departamento']
        widgets = {
            'img_perfil' : forms.ClearableFileInput(attrs = {'class':'form-control mt-2'}),
            'genero' : forms.Select(attrs = {'class':'form-select mt-2'}),
            'tipo_documento' : forms.Select(attrs = {'class':'form-select mt-2'}),
            'numero_documento' : forms.TextInput(attrs = {'class':'form-control mt-2'}),
            'direccion' : forms.Textarea(attrs = {'class':'form-control mt-2', 'rows': '3'}),
            'telefono' : forms.TextInput(attrs = {'class':'form-control mt-2'}),
            'ciudad' : forms.TextInput(attrs = {'class':'form-control mt-2'}),
            'departamento' : forms.TextInput(attrs = {'class':'form-control mt-2'}),
        }

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(help_text='Ingrese un correo por favor.', required=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {k:" " for k in fields}
        
    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
