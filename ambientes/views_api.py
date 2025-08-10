from rest_framework import viewsets
from .models import Ambiente
from .serializers import AmbienteSerializer
from parceiros.permissions import IsAdminEditOrReadOnly
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


method_decorator(csrf_exempt, name='dispatch')
class AmbienteViewSet(viewsets.ModelViewSet):
    queryset = Ambiente.objects.all()
    serializer_class = AmbienteSerializer
    permission_classes = [IsAdminEditOrReadOnly]