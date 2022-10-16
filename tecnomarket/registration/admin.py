from django.contrib import admin
from .models import *

# Register your models here.
class PerfilUsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(PerfilUsuario, PerfilUsuarioAdmin)
