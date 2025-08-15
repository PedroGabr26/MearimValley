from django.urls import path
from .views import instituicoes

urlpatterns = [
    path('', instituicoes, name='mostrar_instituicoes'),
]