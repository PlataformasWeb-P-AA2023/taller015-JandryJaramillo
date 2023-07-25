from django.contrib.auth.models import User, Group
from .models import *

from rest_framework import serializers

class PropietarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Propietario
        fields = "__all__"

class EdificioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Edificio
        fields = "__all__"


class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departamento
        fields = "__all__"
