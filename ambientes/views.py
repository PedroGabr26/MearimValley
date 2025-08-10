from django.shortcuts import render

def ambientes(request):
    return render(request, 'ambientes/ambientes.html')  