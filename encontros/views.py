from django.shortcuts import render


def encontros(request):
    return render(request,'encontros/encontros.html')

