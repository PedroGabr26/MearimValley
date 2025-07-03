from rest_framework import serializers
from .models import Parceiro

class ParceiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parceiro
        fields = '__all__'