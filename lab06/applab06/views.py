from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Producto
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    categorias = Categoria.objects.all()
    product_list = Producto.objects.order_by('nombre')
    context = {'product_list': product_list, 'categorias': categorias}
    return render(request, 'index.html', context)

def producto(request):
    if request.method == 'POST':
        categoria_id = request.POST['categoria']
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        stock = request.POST['stock']
        image = request.FILES['image']

        categoria = Categoria.objects.get(pk=categoria_id)

        producto = Producto(
            categoria=categoria,
            nombre=nombre,
            precio=precio,
            stock=stock,
            image=image
        )
        producto.save()

        return redirect('index')

    categorias = Categoria.objects.all()
    context = {'categorias': categorias}
    return render(request, 'producto.html', context)

def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)

    if request.method == 'POST':
        # Procesar los datos del formulario y guardar los cambios
        categoria_id = request.POST['categoria']
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        stock = request.POST['stock']
        
        # Actualizar los campos del producto
        producto.categoria = Categoria.objects.get(pk=categoria_id)
        producto.nombre = nombre
        producto.precio = precio
        producto.stock = stock

        # Verificar si se proporcionó una nueva imagen
        if 'image' in request.FILES:
            # Eliminar la imagen anterior antes de guardar la nueva
            if producto.image:
                producto.image.delete()

            # Guardar la nueva imagen
            producto.image = request.FILES['image']

        # Guardar los cambios en la base de datos
        producto.save()

        return redirect('index')

    categorias = Categoria.objects.all()
    context = {'producto': producto, 'categorias': categorias}
    return render(request, 'editar_producto.html', context)

def eliminar_producto(request, producto_id):
    # Obtener la instancia del producto o retornar un error 404 si no existe
    producto = get_object_or_404(Producto, pk=producto_id)

    # Eliminar el producto
    producto.delete()

    # Redirigir a la página principal después de la eliminación
    return HttpResponseRedirect(reverse('index'))

def lista_productos(request):
    categoria_filtrada = request.GET.get('categoria')

    if categoria_filtrada:
        productos = Producto.objects.filter(categoria__nombre=categoria_filtrada)
    else:
        productos = Producto.objects.all()

    categorias = Categoria.objects.all()

    context = {
        'productos': productos,
        'categorias': categorias,
    }

    return render(request, 'lista_productos.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')