from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParceiroViewSet

router = DefaultRouter()
router.register(r'parceiros', ParceiroViewSet)

urlpatterns = [
    path('',include(router.urls)),
]

