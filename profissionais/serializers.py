from rest_framework import serializers
from .models import Profissionais

class ProfissionaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profissionais
        fields = '__all__'
