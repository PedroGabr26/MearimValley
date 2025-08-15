from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views_api import EditaisViewSet

router = DefaultRouter()
router.register(r'editais', EditaisViewSet)

urlpatterns = [
    path('', include(router.urls)),
]