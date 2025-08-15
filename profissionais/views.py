from django.shortcuts import render

def profissionais(request):
    return render(request, 'profissionais/profissionais.html')
