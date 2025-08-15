from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views_api import CursosViewSet

router = DefaultRouter()
router.register(r'cursos', CursosViewSet)

urlpatterns = [
    path('', include(router.urls)),
]