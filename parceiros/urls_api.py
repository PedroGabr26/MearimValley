# api_urls - urls da api, urls que levam pro backend

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_api import ParceiroViewSet

router = DefaultRouter()
router.register(r'parceiros', ParceiroViewSet) # Cria AUTOMATICAMENTE TODAS AS ROTAS baesadas em um ModelViewSet. Ele gera todas as rotas como:
'''
GET
POST
PUT
DELETE 
''' 

urlpatterns = [
    path('',include(router.urls)),
]

