from .models import *
from rest_framework import serializers

class BodegaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario_Bodega
        fields = '__all__'

# class ProductoSerializer(serializers.ModelSerializer):
#     nombre_marca = serializers.CharField(read_only=True, source="marca.nombre")
#     marca = MarcaSerializer(read_only=True)
#     marca_id =serializers.PrimaryKeyRelatedField(queryset=Marca.objects.all(), source="marca")
#     nombre = serializers.CharField(required=True, min_length=3)
    
#     def validate_nombre(self, value):
#         existe = Producto.objects.filter(nombre__iexact=value).exists()

#         if existe:
#             raise serializers.ValidationError("Este producto ya existe")
        
#         return value


#     class Meta:
#         model = Producto
#         fields = '__all__'