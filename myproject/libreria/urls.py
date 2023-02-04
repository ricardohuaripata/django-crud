from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static


# Controlador de urls para la aplicacion libreria

urlpatterns = [
    path('', views.index, name='index'),
    path('libros', views.libros, name='libros'),
    path('libros/agregar', views.create, name='create'),
    #path('libros/editar', views.update, name='update'),
    path('libros/borrar/<int:id>', views.delete, name='delete'),
    path('libros/editar/<int:id>', views.update, name='update')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

