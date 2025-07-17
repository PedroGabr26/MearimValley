from django.shortcuts import render

def mostrar_noticias(request):
    return render(request,'noticias/noticias.html')
