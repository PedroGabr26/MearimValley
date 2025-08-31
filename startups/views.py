from django.shortcuts import render


def startups(request):
    return render(request, 'startups/startups.html')

def criar_startup(request):
    return render(request, 'startups/criar_startup.html')
