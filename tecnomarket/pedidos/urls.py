from django.urls import path
from . import views


urlpatterns =[
    path('catalogo/',views.Catalogo.as_view(), name='catalogo'),
    path('categoria/<int:categoria_id>/',views.categoria, name='categoria'),
    #path('marca/<int:marca_id>/',views.marca, name='marca'),
    
    # urls de la API REST
    path('productos/', views.CatalogoApiResponse.as_view(), name='productos'),
    path('producto/<int:pk>/', views.ProductoApiResponse.as_view(), name='producto'),
]


