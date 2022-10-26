from django.urls import path
from django.conf.urls.static import static
from .views import *

urlpatterns =[
    path('catalogo/',Catalogo.as_view(), name='catalogo'),
    #path('categoria/',CategoriaListView.as_view(), name='categoria'),
]

