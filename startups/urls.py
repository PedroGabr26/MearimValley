from django.urls import path
from .views import startups

urlpatterns = [
    path('', startups, name='mostrar_startups')
]
