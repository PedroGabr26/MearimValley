# urls do front end, vai pra página html

from django.urls import path
from .views import *

urlpatterns = [
    path('', parceiros, name='mostrar-parceiros'),
    path('create/',create_parceiro, name='criar-parceiro'),
]

