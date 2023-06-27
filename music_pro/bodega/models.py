from django.db import models
from catalogo.models import *  # Importa todos los modelos

class Inventario_Bodega(models.Model):
    nombre_producto = models.CharField(max_length=50)
    stock = models.IntegerField()
    producto = models.ForeignKey(Producto, on_delete=models.DO_NOTHING)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_producto