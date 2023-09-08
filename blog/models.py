from django.db import models
import datetime
from ckeditor.fields import RichTextField


class Post(models.Model):

    """
    Creamos nuestro post
    RichTextField está muy interesante para poder editar y manipular la descripción a nuestra medida 
    al igual que si queremos añadir imagenes en la descripción, url, emoticonos, vídeos y más cosas.

    """
    title = models.CharField(max_length=100)
    description = RichTextField()
    image = models.ImageField(upload_to="blog/images")
    date = models.DateField(default=datetime.date.today)



    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-id']

   
   
    def __str__(self) -> str:
        return self.title
    
 