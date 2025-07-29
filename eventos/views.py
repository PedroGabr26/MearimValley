from django.shortcuts import render


def eventos(request):
    return render(request, 'eventos/eventos.html')