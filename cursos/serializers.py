from rest_framework import serializers
from .models import Cursos


class CursosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cursos
        fields = '__all__'
