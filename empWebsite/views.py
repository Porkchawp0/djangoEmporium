from django.shortcuts import render, get_object_or_404
from .models import completeProject

# Create your views here.
def projectEmporium(request):
    projects = completeProject.objects.all()
    return render(request, 'emporiumWebsite/index.html', {"projects":projects})

def showLogin(request):
    #login = getInfo(login)
    return render(request, 'emporiumWebsite/login.html')

def showBreakout(request):
    return render(request, 'emporiumWebsite/breakout.html')