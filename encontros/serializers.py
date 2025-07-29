from rest_framework import serializers
from .models import Encontros


class EncontrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encontros
        fields = '__all__'