from django.db import models

# Create your models here.

class Libro(models.Model):
    id_libro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    imagen = models.ImageField(upload_to='imagenes/', null=True, verbose_name='Imagen')
    descripcion = models.TextField(max_length=1000, null=True, verbose_name='Descripcion')

    def __str__(self):
        fila = "ID: %s - Titulo:  %s" % (self.id_libro, self.titulo)
        return fila
#Si borramos un libro se borrara tambien su imagen de la carpeta /imagenes
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()