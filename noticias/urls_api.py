from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views_api import NoticiasViewSet

router = DefaultRouter()
router.register(r'noticias', NoticiasViewSet)

urlpatterns = [
    path('', include(router.urls)),
]