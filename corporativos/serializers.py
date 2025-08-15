from rest_framework import serializers
from .models import Corporativos

class CorporativosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corporativos
        fields = '__all__'

