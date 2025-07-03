from django.shortcuts import render
from .models import Parceiro
from .serializers import ParceiroSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ParceiroViewSet(viewsets.ModelViewSet):
    queryset = Parceiro.objects.all()
    serializer_class = ParceiroSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Todos veêm mas apenas os admin podem editar, criar ou deletar

