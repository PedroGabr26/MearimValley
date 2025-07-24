from django.shortcuts import render

# Create your views here.
def editais(request):
    return render(request, 'editais/editais.html')