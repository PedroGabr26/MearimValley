from django.urls import path
from .views import *

urlpatterns = [
    path('', cursos, name='cursos'),
]