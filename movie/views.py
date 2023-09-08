from django.shortcuts import render,get_object_or_404
from .models import Pelicula, Estreno, Genero
from django.db.models import Q

def home(request):
    """
    Esta parte es igual que en el blog, traemos todas las películas y hacemos un filtrado de búsqueda
    en el que podemos buscar por: título, género, fecha, rate, duración y director, en la barra de búsqueda
    todo esto lo devolvemos en el archivo home.html

    """
    peliculas = Pelicula.objects.all()
    if "buscar" in request.GET:        
        queryset = request.GET.get("buscar")     
        if queryset:                        
            peliculas = Pelicula.objects.filter(
                Q(titulo__icontains = queryset) |               
                Q(genero__nombre__icontains = queryset) |
                Q(fecha__icontains = queryset) |
                Q(rate__icontains = queryset) |
                Q(duracion__icontains = queryset) |
                Q(director__icontains = queryset)
                 
                
            ).distinct()
    
    return render(request, "home.html", {"peliculas": peliculas})


def peliculas(request):
    
    total_peliculas = Pelicula.objects.count()
    peliculas = Pelicula.objects.order_by("-date")
    return render(request, "/", {"peliculas": peliculas, "total_peliculas": total_peliculas})


        
def pelicula_detail(request, pelicula_id):
    pelicula = Pelicula.objects.get(pk=pelicula_id)
    return render(request, 'pelicula_detail.html', {'pelicula': pelicula})

def generos(request):
    generos = Genero.objects.all()
    
    # Resto del código de la vista
    return render(request, 'pelicula_genero.html', {'generos': generos})

def estreno(request):
    estreno = Estreno.objects.all()
    return render(request, 'estreno.html', {'estreno': estreno})


""" def genero(request, genero_id):
    genero = get_object_or_404(Genero, id=genero_id)
    peliculas = Pelicula.objects.filter(generos__id=genero_id)
    context = {'genero': genero, 'peliculas': peliculas}
    return render(request, 'pelicula_genero.html', context)
 """
