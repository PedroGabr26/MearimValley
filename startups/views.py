from django.shortcuts import render


def startups(request):
    return render(request, 'startups/startups.html')