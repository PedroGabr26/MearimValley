from django.urls import path
from .views import ambientes

urlpatterns = [
    path('', ambientes, name='mostrar_ambientes')
]
