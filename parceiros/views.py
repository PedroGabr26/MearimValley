from django.shortcuts import render

def parceiros(request):
    return render(request,'parceiros/parceiros.html')

def create_parceiro(request):
    return render(request, 'parceiros/criar_parceiro.html')