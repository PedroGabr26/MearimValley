from rest_framework import viewsets
from .models import Noticias
from .serializers import NoticiasSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from parceiros.permissions import IsAdminEditOrReadOnly


class NoticiasViewSet(viewsets.ModelViewSet):
    queryset = Noticias.objects.all()
    serializer_class = NoticiasSerializer
    permission_classes = [IsAdminEditOrReadOnly]

