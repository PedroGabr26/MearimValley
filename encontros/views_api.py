from rest_framework import viewsets
from .models import Encontros
from .serializers import EncontrosSerializer
from parceiros.permissions import IsAdminEditOrReadOnly
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class EncontrosViewSet(viewsets.ModelViewSet):
    queryset = Encontros.objects.all()
    serializer_class = EncontrosSerializer
    permission_classes = [IsAdminEditOrReadOnly]
