from django.urls import path, include
from .views import corporativos

urlpatterns = [
    path('', corporativos, name='corporativos')
]