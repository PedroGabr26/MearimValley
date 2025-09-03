from django.shortcuts import render, get_object_or_404
from .models import Noticias

def mostrar_noticias(request):
    return render(request,'noticias/noticias.html')

def noticia_id(request, id):
    noticia = get_object_or_404(Noticias, id=id)
    return render(request, 'noticias/noticia_id.html', {'noticia': noticia})