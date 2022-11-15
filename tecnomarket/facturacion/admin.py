from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import DetallePago, FormaPago, Pedido
# Register your models here.

admin.site.register(FormaPago)
admin.site.register(DetallePago)
admin.site.register(Pedido)