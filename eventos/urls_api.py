from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views_api import EventosViewSet

router = DefaultRouter()
router.register(r'eventos',EventosViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
