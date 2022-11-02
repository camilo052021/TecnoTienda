from unicodedata import name
from django.urls import path
from django.conf.urls.static import static
from . import views


urlpatterns =[
    path('catalogo/',views.Catalogo.as_view(), name='catalogo'),
    #path('categoria/',CategoriaListView.as_view(), name='categoria'),

    # urls para le carro de compras
    path('carro', views.carro, name='carro'),
    path('agregar/<int:producto_id>/', views.agregarProducto, name='agregar'),
    path('eliminar/<int:producto_id>/', views.eliminarProducto, name='eliminar'),
    path('restar/<int:producto_id>/', views.restarProducto, name='restar'),
    path('limpiar/', views.limpiarCarro, name='limpiar'),   

]

