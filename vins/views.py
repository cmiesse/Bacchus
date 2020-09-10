from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Vin


def vins_all(request):
    vins = Vin.objects.all()
    return render(request, 'vins.html', {'vins': vins})

def detailVin(request, vin_id):
    try:
        vin = Vin.objects.get(pk=vin_id)
    except Vin.DoesNotExist:
        raise Http404("Le vin n'existe pas")
    return render(request, 'detailVin.html', {'vin': vin})
