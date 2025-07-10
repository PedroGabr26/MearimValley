from django.shortcuts import render

def mostrar_noticias(request):
    return render(request,'noticias.html')

def criar_noticias(request):
    return render(request, 'criar_noticias.html')