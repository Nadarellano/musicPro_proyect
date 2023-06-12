from django.shortcuts import render
from .models import Producto
from .forms import ContactoForm, ProductoForm

# Create your views here.

def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }

    return render(request, 'catalogo/home.html', data)

def galeria(request):
    return render(request, 'catalogo/galeria.html')

def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Mensaje enviado exitosamente"
        else:
            data["form"] = formulario

    return render(request, 'catalogo/contacto.html', data)

def agregar_producto(request):

    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'catalogo/producto/agregar.html', data)

def listar_productos(request):
        productos = Producto.objects.all()

        data = {
            'productos': productos
        }

        return render(request, 'catalogo/producto/listar.html', data)

