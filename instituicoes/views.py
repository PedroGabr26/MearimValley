from django.shortcuts import render


def instituicoes(request):
    return render(request, 'instituicoes/instituicoes.html')