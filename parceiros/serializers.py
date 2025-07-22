from rest_framework import serializers
from .models import Parceiro

# Faz a ponte entre a instância do modelo Parceiro e a conversão pra JSON e vice versa, pega o JSON e transforma para modelo
class ParceiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parceiro
        fields = '__all__'