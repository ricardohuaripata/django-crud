from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm


# Create your views here.

def index(request):
    return render(request, 'paginas/index.html')

def libros(request):
    #Obtenemos todos los objetos del repositorio de libros
    listaLibros = Libro.objects.all()
    return render(request, 'libros/index.html', {'libros': listaLibros})

def create(request):
    libroFormulario = LibroForm(request.POST or None, request.FILES or None)
    #Si los datos de entrada son validos, se guardara en la base de datos
    #Luego se redireccionara a la pagina de libros
    if libroFormulario.is_valid():
        libroFormulario.save()
        return redirect('libros')
    return render(request, 'libros/create.html', {'formulario': libroFormulario})


def update(request, id):
    #Se obtiene el id del libro a traves del path
    #Se obtiene el objeto con dicho id y se actualiza del repositorio de libros
    libro = Libro.objects.get(id_libro=id)
    libroFormulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)

    if libroFormulario.is_valid() and request.POST:
        libroFormulario.save()
        return redirect('libros')
    return render(request, 'libros/update.html', {'formulario': libroFormulario})

def delete(request, id):
    #Se obtiene el id del libro a traves del path
    #Se obtiene el objeto con dicho id y se elimina del repositorio de libros
    libro = Libro.objects.get(id_libro=id)
    libro.delete()
    return redirect('libros')
