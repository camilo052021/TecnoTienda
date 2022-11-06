from django.urls import path
from . import views


urlpatterns =[
    path('catalogo/',views.Catalogo.as_view(), name='catalogo'),
    path('categoria/<int:categoria_id>/',views.categoria, name='categoria'),
    #path('marca/<int:marca_id>/',views.marca, name='marca'),
]


