from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_api import EncontrosViewSet

router = DefaultRouter()
router.register(r'encontros', EncontrosViewSet)

urlpatterns = [
    path('', include(router.urls)),
]