from django.urls import path
from .views import profissionais

urlpatterns = [
    path('', profissionais, name='mostrar_profissionais')
]
