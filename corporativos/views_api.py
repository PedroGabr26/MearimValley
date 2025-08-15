from rest_framework import viewsets
from .serializers import CorporativosSerializer
from .models import Corporativos
from parceiros.permissions import IsAdminEditOrReadOnly
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


method_decorator(csrf_exempt, name='dispatch')
class CorporativosViewSet(viewsets.ModelViewSet):
    queryset = Corporativos.objects.all()
    serializer_class = CorporativosSerializer
    permission_classes = [IsAdminEditOrReadOnly]

