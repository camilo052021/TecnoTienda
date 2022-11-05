from django.urls import path
from . import views


urlpatterns =[
    path('catalogo/',views.Catalogo.as_view(), name='catalogo'),
    #path('categoria/',CategoriaListView.as_view(), name='categoria'),
]


