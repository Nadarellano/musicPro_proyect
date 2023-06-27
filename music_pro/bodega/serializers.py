from .models import *
from rest_framework import serializers

class BodegaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario_Bodega
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
     class Meta:
        model = Producto
        fields = '__all__'