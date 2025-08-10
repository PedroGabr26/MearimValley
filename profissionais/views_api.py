from rest_framework import viewsets
from .models import Profissionais
from .serializers import ProfissionaisSerializer
from parceiros.permissions import IsAdminEditOrReadOnly
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


method_decorator(csrf_exempt, name='dispatch')
class ProfissionaisViewSet(viewsets.ModelViewSet):
    queryset = Profissionais.objects.all()
    serializer_class = ProfissionaisSerializer
    permission_classes = [IsAdminEditOrReadOnly]