from django.urls import path
from .views import startups, criar_startup

urlpatterns = [
    path('', startups, name='mostrar_startups'),
    path('create/', criar_startup, name='criar_startup')
]
