from rest_framework import viewsets
from .models import Instituicoes
from .serializers import InstituicoesSerializer
from parceiros.permissions import IsAdminEditOrReadOnly
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


method_decorator(csrf_exempt, name='dispatch')
class InstituicaoViewSet(viewsets.ModelViewSet):
    queryset = Instituicoes.objects.all()
    serializer_class = InstituicoesSerializer
    permission_classes = [IsAdminEditOrReadOnly]
