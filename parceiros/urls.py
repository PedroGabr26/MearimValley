# urls do front end, vai pra página html

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

urlpatterns = [
    path('parceiros/', parceiros, name='mostrar-parceiros'),
    path('create_parceiro/',create_parceiro, name='criar-parceiro'),
]

