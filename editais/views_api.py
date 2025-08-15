from rest_framework import viewsets
from .models import Editais
from .serializers import EditaisSerializers
from parceiros.permissions import IsAdminEditOrReadOnly
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt,name='dispatch')
class EditaisViewSet(viewsets.ModelViewSet):
    queryset = Editais.objects.all()
    serializer_class = EditaisSerializers
    permission_classes = [IsAdminEditOrReadOnly]