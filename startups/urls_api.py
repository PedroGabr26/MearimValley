from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_api import StartupViewSet

router = DefaultRouter()
router.register(r'startups', StartupViewSet)

urlpatterns = [
    path('', include(router.urls))
]