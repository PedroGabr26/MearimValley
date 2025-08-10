from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_api import ProfissionaisViewSet


router = DefaultRouter()
router.register(r'profissionais', ProfissionaisViewSet)

urlpatterns = [
    path('', include(router.urls))
]
