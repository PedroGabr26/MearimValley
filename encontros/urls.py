from django.urls import path
from .views import encontros

urlpatterns = [
    path('', encontros, name='encontros'),
]
