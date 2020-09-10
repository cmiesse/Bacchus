from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Soiree

def index(request):
    soirees = Soiree.objects.all().order_by('-date')
    return render(request, 'index.html', {'soirees': soirees})

def detailSoiree(request, soiree_id):
    try:
        soiree = Soiree.objects.get(pk=soiree_id)
    except Soiree.DoesNotExist:
        raise Http404("La soirée n'existe pas")
    return render(request, 'detailSoiree.html', {'soiree': soiree})
