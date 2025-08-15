# urls do front end, vai pra página html

from django.urls import path
from .views import *

urlpatterns = [
    path('', editais, name='editais'),
]