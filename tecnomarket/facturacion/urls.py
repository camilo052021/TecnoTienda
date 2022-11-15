from django.urls import path
#from .views import GenerarPDF
from . import views


urlpatterns =[
    path('factura/',views.factura, name='factura'),
    path('ejemplopdf/', views.GeneratePdf.as_view(), name = 'ejemplopdf'),
    #path('pago/',  views.PasarelaPago.as_view(), name = 'pago'),
    path('pago/',  views.pago, name = 'pago'),
    path("procesar_pedido/", views.procesar_pedido, name="procesar_pedido"),
    
]
