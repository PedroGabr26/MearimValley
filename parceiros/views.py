from django.shortcuts import render

def parceiros(request):
    return render(request,'parceiros.html')

def create_parceiro(request):
    return render(request, 'criar_parceiro.html')