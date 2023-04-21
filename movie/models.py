from django.db import models

from django.db import models
from django.db.models.fields import CharField, DateField, URLField
from django.db.models.fields.files import ImageField
from datetime import date




class Genero(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    

class Pelicula(models.Model):
    titulo = CharField(max_length=100)
    descripcion = models.TextField()
    imagen = ImageField(upload_to="movie/images")
    genero = models.ManyToManyField(Genero)
    duracion = CharField(max_length=10)
    rate = CharField(max_length=6)
    url = URLField(blank=True)
    trailer = URLField(blank=True)
    fecha = DateField(default=date.today)
    director = CharField(max_length=50)
    reparto = models.TextField()

    def __str__(self) -> str:
        return self.titulo


class Estreno(models.Model):
    titulo = CharField(max_length=100)
    fecha_estreno = DateField(default=date.today)
    imagen = ImageField(upload_to="estreno/images")


    def __str__(self) -> str:
        return self.titulo