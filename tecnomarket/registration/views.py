from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model, login
from .forms import UserRegisterForm, PerfilForm, UserUpdateForm
from django.contrib import messages
from django import forms
from django.urls import reverse_lazy
# Importamos el modelo de datos
from .models import PerfilUsuario
# Decoradores del Login:
from django.utils.decorators import method_decorator        # Método decorador para usuario logueado y uso de la vista:
from django.contrib.auth.decorators import login_required   # Método de requiere inicio de sesión:
# Implementar Vistas Bassadas en Clases de Django:
from django.views.generic.edit import UpdateView

# Create your views here.
def register(request):
    #El usuario que ha iniciado sesión no puede registrar una nueva cuenta
    if request.user.is_authenticated:
        return redirect("/")
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro Exitoso." )
            return redirect("/")
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = UserRegisterForm()

    context = {'form':form}
    return render(request, 'registration/register.html', context)    


@method_decorator(login_required, name='dispatch')
class PerfilUpdate(UpdateView):
    form_class =  PerfilForm
    success_url =  reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    # Sobreescribimos el método get_object:
    def get_object(self):
        perfil, creado = PerfilUsuario.objects.get_or_create(usuario=self.request.user)
        return perfil


@login_required
def editRegister(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserUpdateForm(instance=request.user)
  
    context = {'form': form}
    return render(request, 'registration/edit_register.html', context)