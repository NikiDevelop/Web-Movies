from django.shortcuts import render, get_object_or_404
from .models import Post
from django.db.models import Q


def renderPosts(request):

    """
    Traemos los posts que están ordenados de más recientes a antiguos.
    Hacemos una filtración de los posts mediante búsqueda de título o fecha en la barra de búsqueda que 
    hemos creado en base.html 
    
    """    
    posts = Post.objects.order_by("-date")

    if "buscar" in request.GET:
        queryset = request.GET.get("buscar")
        if queryset:                        
            posts = Post.objects.filter(
                Q(title__icontains = queryset) | 
                Q(date__icontains = queryset)                 
                
            ).distinct()

    return render(request, "blog.html", {"posts": posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "post_detail.html", {"post": post})
