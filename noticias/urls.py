# urls do front end, vai pra página html

from django.urls import path
from .views import *

urlpatterns = [
    path('', mostrar_noticias, name='mostrar_noticias'),
    # path('create/', criar_noticias, name='criar_noticias'),
]