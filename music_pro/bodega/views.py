from django.shortcuts import render
from rest_framework import viewsets

from .serializers import *
from .models import *
# Create your views here.

class BodegaViewset(viewsets.ModelViewSet):
    queryset = Inventario_Bodega.objects.all()
    serializer_class = BodegaSerializer
