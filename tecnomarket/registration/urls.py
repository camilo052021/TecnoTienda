from django.urls import path
from .views import register, PerfilUpdate, editRegister
# importamos las funciones integradas de django para login y logout
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),

    ## registro del perfil
    path('profile/', PerfilUpdate.as_view(), name='profile'),
    path('edit_register/', editRegister, name='edit_register'),
]
