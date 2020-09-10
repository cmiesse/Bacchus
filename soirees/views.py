from django.http import HttpResponse
from django.shortcuts import render
from .models import Soiree

def index(request):
    soirees = Soiree.objects.all()
    return render(request, 'index.html', {'soirees': soirees})
