# urls do front end, vai pra página html

from django.urls import path
from .views import *

urlpatterns = [
    path('', mostrar_noticias, name='mostrar_noticias'),
    path('<int:id>/', noticia_id, name='noticia_id'),
]