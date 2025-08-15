from rest_framework import viewsets
from .models import Cursos
from .serializers import CursosSerializer
from parceiros.permissions import IsAdminEditOrReadOnly
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class CursosViewSet(viewsets.ModelViewSet):
    queryset = Cursos.objects.all()
    serializer_class = CursosSerializer
    permission_classes = [IsAdminEditOrReadOnly]