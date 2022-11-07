from django.urls import path
from . import views


urlpatterns =[
    path('factura/',views.factura, name='factura'),
]
