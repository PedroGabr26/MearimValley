from rest_framework import serializers
from .models import Editais

class EditaisSerializers(serializers.ModelSerializer):
    class Meta:
        model = Editais
        fields = '__all__'