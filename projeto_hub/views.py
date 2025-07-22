from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def sobre(request):
    return render(request, 'sobre.html')

def contatos(request):
    return render(request, 'contatos.html')