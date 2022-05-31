from django.shortcuts import render
from django.http import HttpResponse
from Familiapp.models import Familiares

# Create your views here.

def inicio(request):
    return HttpResponse('Bienvenid@')

def familiares(request):
    familiares = Familiares.objects.all()
    return render(request, 'Familiapp.html', {'familiares': familiares})
