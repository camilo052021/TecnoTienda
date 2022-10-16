import imp
from django.urls import path
from django.conf.urls.static import static
from src import settings
from django.conf import settings
from .views import *

urlpatterns =[
    path('catalogo/',catalogo, name='catalogo'),
]
