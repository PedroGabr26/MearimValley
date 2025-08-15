from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_api import CorporativosViewSet 


router = DefaultRouter()
router.register(r'corporativos', CorporativosViewSet)

urlpatterns = [
    path('', include(router.urls))
]