from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Producto
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    product_list = Producto.objects.order_by('nombre')
    context = {'product_list': product_list}
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
            producto.image = request.FILES['image']

        # Guardar los cambios en la base de datos
        producto.save()

        # Imprimir un mensaje para verificar que llegó aquí
        print("Cambios guardados exitosamente")

        return redirect('index')

    context = {'producto': producto}
    return render(request, 'editar_producto.html', context)

def eliminar_producto(request, producto_id):
    # Obtener la instancia del producto o retornar un error 404 si no existe
    producto = get_object_or_404(Producto, pk=producto_id)

    # Eliminar el producto
    producto.delete()

    # Redirigir a la página principal después de la eliminación
    return HttpResponseRedirect(reverse('index'))