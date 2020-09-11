from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Fiche


def fiches_all(request):
    fiches = Fiche.objects.all()
    return render(request, 'fiches.html', {'fiches': fiches})

def detailFiche(request, fiche_id):
    try:
        fiche = Fiche.objects.get(pk=fiche_id)
    except Fiche.DoesNotExist:
        raise Http404("La fiche n'existe pas")
    return render(request, 'detailFiche.html', {'fiche': fiche})
