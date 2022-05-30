from django.shortcuts import render
from rest_framework import viewsets
from .models import Symbol
from .serializers import SymbolSerializer

# Create your views here.
class SymbolView(viewsets.ModelViewSet):
    queryset = Symbol.objects.all()
    serializer_class = SymbolSerializer
    
