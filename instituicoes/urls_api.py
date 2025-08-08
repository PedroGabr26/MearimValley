from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_api import InstituicaoViewSet

router = DefaultRouter()
router.register(r'instituicoes', InstituicaoViewSet)

urlpatterns = [
    path('', include(router.urls))
]
