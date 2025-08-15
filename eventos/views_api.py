from rest_framework import viewsets
from .models import Eventos
from .serializers import EventosSerializer
from parceiros.permissions import IsAdminEditOrReadOnly
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class EventosViewSet(viewsets.ModelViewSet):
    queryset = Eventos.objects.all()
    serializer_class = EventosSerializer
    permission_classes = [IsAdminEditOrReadOnly]
