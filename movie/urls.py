
from django.urls import path
from movie import views
from django.conf import settings
from django.conf.urls.static import static
from .models import Genero


urlpatterns = [
    
    path('', views.home, name="Home"),
    
    path('pelicula/<int:pelicula_id>/', views.pelicula_detail, name='pelicula_detail'),
    path('genero/', views.generos, name='genero'),
    path('estreno/', views.estreno, name='estreno'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)