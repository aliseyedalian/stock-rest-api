from rest_framework import serializers
from .models import Symbol

class SymbolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Symbol
        fields = '__all__'
