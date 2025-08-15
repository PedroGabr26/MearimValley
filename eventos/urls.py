from django.urls import path
from .views import eventos

urlpatterns = [
    path('', eventos, name='eventos')
]