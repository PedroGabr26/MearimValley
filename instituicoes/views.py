from django.shortcuts import render


def instituicoes(request):
    return render(request, 'instituicoes/instituicoes.html')

def criar_instituicao(request):
    return render(request, 'instituicoes/criar_instituicao.html')