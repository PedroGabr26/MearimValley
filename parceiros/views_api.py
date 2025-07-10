from rest_framework import viewsets
from .models import Parceiro
from .serializers import ParceiroSerializer
from .permissions import IsAdminEditOrReadOnly
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class ParceiroViewSet(viewsets.ModelViewSet): # viewssets.ModelViewSet - Faz com que a api de parceiros já venha com os métodoS e URLs padrão:
    # - GET /parceiros/ → listar todos     - POST /parceiros/ → criar novo      - GET /parceiros/<id>/ → buscar um       - PUT /parceiros/<id>/ → atualizar     - DELETE /parceiros/<id>/ → excluir
    queryset = Parceiro.objects.all() # diz os objetos e a quantidade deles que vamos trabalhar na nossa api
    serializer_class = ParceiroSerializer # é quem vai fazer a ponte, A CONVERSÃO entre :  objeto do modelo <-> dados em JSON
    permission_classes = [IsAdminEditOrReadOnly] # Controla Permissão. Qualquer um pode ler(GET), mas os outros métodos 