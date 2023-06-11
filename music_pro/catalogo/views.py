from django.shortcuts import render
from .models import Producto

# Create your views here.

def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }

    return render(request, 'catalogo/home.html', data)

def galeria(request):
    return render(request, 'catalogo/galeria.html')