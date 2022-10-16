from django.db import models
# Paso 1: Importamos de Django el modelo de datos de Usuario:
from django.contrib.auth.models import User
# Paso 2: Importo de la clase constrain el metodo CASCADE:
from django.db.models.deletion import CASCADE
# Paso 3: Importar modulo de cambios receiver
from django.dispatch import receiver
# Paso 4: Importar el metodo para sobreescribirlo
from django.db.models.signals import post_save
# Paso 5: Incluir Types:
from app.types.generos import generos
from app.types.tipoid import tiposidentificacion

# Paso 6: Función Global para guardar imagen de perfil de usuario:
def subir_avatar(instance, archivo):
    anterior_instancia = PerfilUsuario.objects.get(pk=instance.pk)
    anterior_instancia.img_perfil.delete()
    return 'static/img/imgprofile' + archivo

# Paso 7: Create your models here.
class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=CASCADE,verbose_name = "Usuario")
    img_perfil = models.ImageField(upload_to= subir_avatar, null = True, blank = True,verbose_name = "ImgPerfil",default='static/img/imgperfil/default.png')
    genero = models.CharField(max_length=20,choices=generos, null =  False, default = 'Otro', verbose_name = "Género")
    tipo_documento = models.CharField(max_length=50,choices=tiposidentificacion, null =  False, default = 'Sin Identificar', verbose_name = "Tipo Documento")
    numero_documento = models.CharField(max_length=50, null =  False, verbose_name = "Número Documento")
    direccion = models.TextField(verbose_name = "Dirección", null= True, blank= True)
    telefono = models.CharField(max_length=10, null= True, blank= True, verbose_name = "Número Teléfono")
    ciudad = models.CharField(max_length=50, null= True, blank= True, verbose_name = "Ciudad")
    departamento = models.CharField(max_length=50, null= True, blank= True, verbose_name = "Departamento")
    #Atributos de auditoría
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha Modificación")

    # Metadata del Modelo:
    class Meta:
        verbose_name = 'Perfil Usuario'
        verbose_name_plural = 'Perfiles Usuarios'
        ordering = ['usuario']
        
    def __str__(self):
       return self.usuario.username
# Función usa decoradores para usuarios que se encuentren creados:
@receiver(post_save, sender=User)
def ensure_profile_exist(sender, instance, **kwargs):
    if kwargs.get('created', False):
        PerfilUsuario.objects.get_or_create(usuario=instance)
