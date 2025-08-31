from django.urls import path
from .views import instituicoes, criar_instituicao

urlpatterns = [
    path('', instituicoes, name='mostrar_instituicoes'),
    path('create/', criar_instituicao, name='criar_instituicao')
]