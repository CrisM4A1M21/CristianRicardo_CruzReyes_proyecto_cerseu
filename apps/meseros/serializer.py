from rest_framework import serializers
from .models import Meseros


class MeseroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meseros
        fields = ('nombre', 'nacionalidad', 'edad', 'procedencia')
